from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
import django.contrib.auth.urls

from . import views
from .views import *

urlpatterns = [
    path('', include("django.contrib.auth.urls")),
    path('login/', views.login_view, name='login_view'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

