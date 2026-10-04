from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import RegisterForm, StyledAuthForm
from .models import BannerImage
from django.contrib.auth.decorators import login_required


def main_page(request):
    banner = BannerImage.objects.last()

    context = {
        'banner': banner
    }

    return render(request, 'main/index.html', context)

def register_page(request):
    if request.user.is_authenticated:
        return redirect('main:home')

    elif request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("main:home")
    else:
        form = RegisterForm()
    return render(request, "main/register.html", {"form": form})


def login_page(request):
    if request.user.is_authenticated:
        return redirect('main:home')

    elif request.method == "POST":
        form = StyledAuthForm(request, data=request.POST)

        if form.is_valid():
            login(request, form.get_user())
            return redirect("main:home")
    else:
        form = StyledAuthForm()

    return render(request, "main/login.html", {"form": form})


def logout_func(request):
    logout(request)
    return redirect("main:login")

def profile_page(request):
    return render(request, 'main/profile.html')

@login_required
def profile_page(request):
    context = {
        'user': request.user,
    }

    return render(request, 'main/profile.html', context)