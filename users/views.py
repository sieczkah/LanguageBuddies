from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.decorators.debug import sensitive_variables

from rooms.models import Language

from .forms import ProfileForm, UserForm
from .models import Profile


# Create your views here.
@sensitive_variables("username", "pw")
def login_view(request):
    # Page name to handle the login/register template
    page = "login"

    # Avoiding log in users login page via url
    if request.user.is_authenticated:
        return redirect("home")

    # Checking if request is POST, authenticating user and login in if authenticated
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            redirect_link = request.GET.get("next", default="home")
            return redirect(redirect_link)
    else:
        form = AuthenticationForm()

    context = {"page": page, "form": form}
    return render(request, "users/login.html", context)


def logout_view(request):
    logout(request)
    return redirect("home")


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_profile = Profile.objects.create(user=new_user)
            login(request, new_user)
            return redirect("home")
    else:
        form = UserCreationForm()

    context = {"form": form}
    return render(request, "users/login.html", context)


def profile_view(request, id):
    user = User.objects.get(id=id)
    fullname = user.get_full_name()
    rooms = user.room_set.all()
    room_messages = user.message_set.all()
    talking_langs = Language.objects.filter(room__members=user).distinct()

    context = {
        "viewed_user": user,
        "rooms": rooms,
        "room_messages": room_messages,
        "fullname": fullname,
        "talking_langs": talking_langs,
    }

    return render(request, "users/profile.html", context)


@login_required
def edit_profile_view(request):
    user = request.user
    user_form = UserForm(instance=user)
    profile_form = ProfileForm(instance=user.profile)

    if request.method == "POST":
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, instance=user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("profile", id=user.id)
        else:
            messages.error(request, "Something went wrong, check your inputs")

    context = {"user_form": user_form, "profile_form": profile_form}
    return render(request, "users/edit_profile.html", context)
