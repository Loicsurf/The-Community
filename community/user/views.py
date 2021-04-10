from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm,UserUpdateForm, ProfileUpdateForm

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)

        return redirect("login")
    else:
        form = RegisterForm()

    return render(response, "register.html", {"form": form})
@login_required

def profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, 
		request.FILES, 
		instance=request.user)

		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your account has been updated!')
			return redirect('profile')
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user)

	context = {
		'u_form': u_form,
		'p_form': p_form
	}
	return render(request, 'profile.html', context)