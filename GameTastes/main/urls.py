from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('account', views.account, name='account'),
    path('all_recipes', views.all_recipes.as_view(), name='all_recipes'),
    path('recipe/<int:pk>', views.recipe.as_view(), name='recipe'),
    path('gradesAdd/<int:pk>', views.gradesAdd, name='gradesAdd'),
    path('favoriteAdd/<int:pk>', views.favoriteAdd, name='favoriteAdd'),
    path('favorites', views.favorites, name='favorites'),
    path('about', views.about, name='about'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
