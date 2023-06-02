from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import RoomEditForm, RoomForm, UserForm
from .models import Language, Message, Room


def login_view(request):
    # Page name to handle the login/register template
    page = "login"

    # Avoiding log in users accessing /accounts/login/ page via url
    if request.user.is_authenticated:
        return redirect("homepage")

    # Checking if request is POST, authenticating user and login in if authenticated
    if request.method == "POST":
        username = request.POST["username"].lower()
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            redirect_link = request.GET.get("next", default="homepage")
            return redirect(redirect_link)
        else:
            # If failed to authenticate sends back error message
            messages.error(request, "Incorrect username or password.")

    context = {"page": page}
    return render(request, "base/login.html", context)


def logout_view(request):
    logout(request)
    return redirect("homepage")


def register_view(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.username = new_user.username.lower()
            new_user.save()
            login(request, new_user)
            return redirect("homepage")

    context = {"form": form}
    return render(request, "base/login.html", context)


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
    return render(request, "base/home.html", context)


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
    return render(request, "base/room.html", context)


def profile_view(request, id):
    user = User.objects.get(id=id)
    fullname = user.get_full_name()
    rooms = user.room_set.all()
    room_messages = user.message_set.all()

    context = {
        "user": user,
        "rooms": rooms,
        "room_messages": room_messages,
        "fullname": fullname,
    }
    return render(request, "base/profile.html", context)


@login_required
def edit_profile_view(request):
    user = request.user
    form = UserForm(instance=user)

    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("profile", id=user.id)

    context = {"form": form}
    return render(request, "base/edit_profile.html", context)


@login_required
def create_room(request):
    form = RoomForm()

    if request.method == "POST":
        form = RoomForm(request.POST)

        if form.is_valid():
            room = form.save(commit=False)
            room.host = request.user
            room.save()
            return redirect("homepage")

    context = {"form": form}
    return render(request, "base/room_form.html", context)


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
            return redirect("homepage")

    context = {"form": form}
    return render(request, "base/room_form.html", context)


@login_required
def delete_room(request, id):
    room = Room.objects.get(id=id)
    if request.user != room.host:
        return HttpResponse("You don't own this room, or you are not logged in")
    else:
        room.delete()
        return redirect("homepage")


@login_required
def delete_message(request, id):
    msg = Message.objects.get(id=id)
    room_id = msg.room.id
    if request.user != msg.user:
        return HttpResponse("Nice try.")
    else:
        msg.delete()
        return redirect("room", id=room_id)
