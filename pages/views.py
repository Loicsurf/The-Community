from django.shortcuts import render

def home(request):
	return render(request, 'home.html', {})

def services(request):
	return render(request, 'services.html', {})

def about(request):
	return render(request, 'about.html', {})

def portfolio(request):
	return render(request, 'portfolio.html', {})

def login(request):
	return render(request, 'login.html', {})