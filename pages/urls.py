from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views
from user import views as v
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
	path('', views.home, name='home'),
    path('services', views.services, name='services'),
    path('about', views.about, name='about'),
    path('portfolio', views.portfolio, name='portfolio'),
    path("register/", v.register, name="register"),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)