from django.http import request
from django.shortcuts import render, redirect
from .forms import RegisterForm

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)

        return redirect("login")
    else:
        form = RegisterForm()

    return render(response, "register.html", {"form": form})

def date(response):
    return render(request, {'form':date})