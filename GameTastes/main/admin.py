from django.contrib import admin

from . import models
from .models import Favorites, Games, Genres, Ingredients, RecipeIngredients, Units, Recipes, Instructions, Grades

# Register your models here.
admin.site.register(Favorites)
admin.site.register(Games)
admin.site.register(Genres)
admin.site.register(Ingredients)
admin.site.register(RecipeIngredients)
admin.site.register(Units)
admin.site.register(Instructions)
admin.site.register(Grades)

@admin.register(models.Recipes)
class PostModelAdmin(admin.ModelAdmin):
    search_fields = ('idGame_id', 'idGame')