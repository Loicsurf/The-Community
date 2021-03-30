from django.urls import path, include
from django.contrib import admin
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
    path("login/", views.login, name="login"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)