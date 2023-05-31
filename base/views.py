from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Room, Language, Message
from .forms import RoomForm, RoomEditForm


def login_view(request):

    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            redirect_link = request.GET.get('next', default='homepage')
            return redirect(redirect_link)
        else:
            messages.error(request, 'Incorrect username or password.')

    context={}
    return render(request, 'base/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('homepage')
# Create your views here.
def home(request):
    q = request.GET.get('q', default='')
    if q.startswith('@'):
        q = q[1:]
        rooms = Room.objects.filter(host__username__icontains=q)
    else:
        rooms = Room.objects.filter(
            Q(language__name__icontains=q) |
            Q(name__icontains=q)
            )

    languages = Language.objects.all()

    context = {'rooms': rooms, 'languages': languages}
    return render(request, "base/home.html", context)


def room(request, id):
    room = Room.objects.get(id=id)
    context = {'room': room}
    return render(request, "base/room.html", context)

@login_required
def create_room(request):
    form = RoomForm()

    if request.method == 'POST':
        form = RoomForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('homepage')
        
    context = {'form': form}
    return render(request, "base/room_form.html", context)


def update_room(request, id):
    room = Room.objects.get(id=id)
    form = RoomEditForm(instance=room)

    if request.method == 'POST':
        form = RoomEditForm(request.POST, instance=room)

        if form.is_valid():
            form.save()
            return redirect('homepage')
        
    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def delete_room(request, id):
    room = Room.objects.get(id=id)
    room.delete()
    return redirect('homepage')