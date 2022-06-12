from email import message
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, ProfileForm
from django.contrib import messages

from django.views.generic import TemplateView

from users.models import Profile

# Create your views here.


class HomeView(TemplateView):
    Model = Profile
    template_name: str = "home.html"


def logout_view(request):
    logout(request)
    messages.info(request, "User was successfully logged out")
    return redirect("/")


def register_view(request):
    if request.user.is_authenticated:
        return redirect("user_account")
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            Profile.objects.get_or_create(
                user=user,
                username=user.username,
                email=user.email,
                first_name=user.first_name,
                last_name=user.last_name,
            )

            messages.success(request, "User was successfully created")
            login(request, user, backend="django.contrib.auth.backends.ModelBackend")
            return redirect("update")
    else:
        form = CustomUserCreationForm()

    return render(request, "users/register.html", {"form": form})


@login_required(login_url="login")
def user_account_view(request):
    profile = request.user.profile
    return render(request, "users/account.html", {"profile": profile})


@login_required(login_url="login")
def update_account_view(request):

    if request.method == "POST":

        profile_form = ProfileForm(
            request.POST, request.FILES, instance=request.user.profile
        )

        if profile_form.is_valid():
            try:
                profile_form.save()
                messages.info(request, "Profile updated successfully")
                return redirect("user_account")
            except:
                messages.warning(request, "Username already exist")

    else:
        profile_form = ProfileForm(instance=request.user.profile)

    context = {"profile_form": profile_form}
    return render(request, "users/edit.html", context)
