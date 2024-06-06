from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
import django.contrib.auth.urls

from . import views
from .views import RegisterView

urlpatterns = [
    path('', include("django.contrib.auth.urls")),
    path('login/', views.login, name='login'),
    path('profile', views.profile, name='profile'),
    path('register', RegisterView.as_view(), name='register'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
