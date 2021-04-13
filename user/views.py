from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)

        return redirect("login")
    else:
        form = RegisterForm()

    return render(response, "register.html", {"form": form})