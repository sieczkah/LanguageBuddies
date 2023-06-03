from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.debug import sensitive_variables

from .forms import RoomEditForm, RoomForm
from .models import Language, Message, Room


# Create your views here.
def home(request):
    q = request.GET.get("q", default="")
    total_room_count = Room.objects.all().count()

    if q.startswith("@"):
        lookup_user = q[1:]
        rooms = Room.objects.filter(host__username__icontains=lookup_user)
        room_messages = Message.objects.filter(Q(user__username__icontains=lookup_user))

    else:
        rooms = Room.objects.filter(
            Q(language__name__icontains=q) | Q(name__icontains=q)
        )
        room_messages = Message.objects.filter(
            Q(room__language__name__icontains=q) | Q(room__name__icontains=q)
        )

    languages = Language.objects.all()

    context = {
        "rooms": rooms,
        "languages": languages,
        "room_messages": room_messages,
        "total_room_count": total_room_count,
        "param": q,
    }
    return render(request, "rooms/home.html", context)


def room(request, id):
    room = Room.objects.get(id=id)
    messages = room.message_set.all().order_by("sent")
    members = room.members.all()

    # Sending a message
    if request.method == "POST":
        message = Message.objects.create(
            user=request.user, room=room, body=request.POST.get("body")
        )
        # Automatically adding a member to the room if texted
        room.members.add(request.user)

        return redirect("room", id=room.id)

    context = {"room": room, "messages": messages, "members": members}
    return render(request, "rooms/room.html", context)


@login_required
def create_room(request):
    form = RoomForm()

    if request.method == "POST":
        form = RoomForm(request.POST)

        if form.is_valid():
            room = form.save(commit=False)
            room.host = request.user
            room.save()
            return redirect("home")

    context = {"form": form}
    return render(request, "rooms/room_form.html", context)


@login_required
def update_room(request, id):
    room = Room.objects.get(id=id)

    if request.user != room.host:
        return HttpResponse("You don't own this room, or you are not logged in")

    form = RoomEditForm(instance=room)

    if request.method == "POST":
        form = RoomEditForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {"form": form, "room": room}
    return render(request, "rooms/edit_room.html", context)


@login_required
def delete_room(request, id):
    room = Room.objects.get(id=id)
    if request.user != room.host:
        return HttpResponse("You don't own this room, or you are not logged in")
    else:
        room.delete()
        return redirect("home")


@login_required
def delete_message(request, id):
    msg = Message.objects.get(id=id)
    room_id = msg.room.id
    if request.user != msg.user:
        return HttpResponse("Nice try.")
    else:
        msg.delete()
        return redirect("room", id=room_id)
