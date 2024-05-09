from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('account', views.account, name='account'),
    path('all_recipes', views.all_recipes, name='all_recipes'),
    path('recipe', views.recipe, name='recipe'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

