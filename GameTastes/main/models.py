from django.contrib.auth.models import User
from django.db import models

# Create your models here.






class Genres(models.Model):
    name = models.CharField(max_length=256)
    def __str__(self):
        return f'Жанр: {self.name}'

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

class Games(models.Model):
    name = models.CharField(max_length=100)
    idGenre = models.ForeignKey(Genres, on_delete=models.CASCADE)
    description = models.CharField(max_length=2048)
    yIssue = models.IntegerField()
    image = models.ImageField('Картинка', upload_to='images', null=True)
    def __str__(self):
        return f'Игра: {self.name}'

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'



class Ingredients(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название')
    image = models.ImageField('Картинка', upload_to='images', null=True)
    def __str__(self):
        return f'Игридиент: {self.name}'

    class Meta:
        verbose_name = 'Игридиент'
        verbose_name_plural = 'Ингридиенты'



class Units(models.Model):
    name = models.CharField(max_length=32)
    def __str__(self):
        return f'Единица измерения: {self.name}'

    class Meta:
        verbose_name = 'Единица измерения'
        verbose_name_plural = 'Единицы измерения'

class Recipes(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название')
    nameInGame = models.CharField(max_length=256, verbose_name='Как называется в игре', default='Неизвестно')
    image = models.ImageField('Фото', upload_to='images', null=True)
    description = models.CharField(max_length=4096, verbose_name='Описание')
    cookingFullTime = models.IntegerField()
    cookingTime = models.IntegerField()
    portions = models.IntegerField()
    lvlComplexity = models.IntegerField()
    idGame = models.ForeignKey(Games, on_delete=models.CASCADE)
    grade = models.IntegerField(default=0)
    calories = models.FloatField(default=0)
    squirrels = models.FloatField(default=0)
    fats = models.FloatField(default=0)
    carbohydrates = models.FloatField(default=0)

class RecipeIngredients(models.Model):
    idRecipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    idIngredient = models.ForeignKey(Ingredients, on_delete=models.CASCADE)
    amount = models.FloatField()
    idUnit = models.ForeignKey(Units, on_delete=models.CASCADE)
    def __str__(self):
        return f'Игридиент для рецепта: {self.idRecipe.name}'

    class Meta:
        verbose_name = 'Игридиент для рецепта'
        verbose_name_plural = 'Игридиенты для рецептов'

class Instructions(models.Model):
    idRecipe = models.ForeignKey(Recipes, on_delete=models.CASCADE, default=123)
    description = models.CharField(max_length=2056, verbose_name='Описание')
    step = models.IntegerField(verbose_name='Шаг')
    image = models.ImageField('Фото', upload_to='images', null=True)

    def __str__(self):
        return f'Инструкция для рецепта: {self.idRecipe.name}'

    class Meta:
        verbose_name = 'Инструкция для рецепта'
        verbose_name_plural = 'Инструкции для рецепта'

class Grades(models.Model):
    idUser = models.ForeignKey(User, on_delete=models.CASCADE)
    idRecipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    lvl = models.IntegerField()

class Favorites(models.Model):
    idRecipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    idUser = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f'Избранное рецепта: {self.idRecipe.name}'

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'


