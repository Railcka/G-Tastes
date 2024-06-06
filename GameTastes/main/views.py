from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView

from .filters import GamesFilter
from .forms import GradesForm, FavoritesForm
from .models import Recipes, RecipeIngredients, Instructions, Grades, Favorites


# Create your views here.


def index(request):
    return render(request, 'main/index.html', {'title': 'Главная страница'})


class all_recipes(ListView):

    model = Recipes
    template_name = 'main/all_recipes.html'
    context_object_name = 'recipes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filtersGames'] = GamesFilter(self.request.GET,
                                                 queryset=Recipes.objects.all().order_by(
                                                     '-pk'))
        context['recipesObjects'] = Recipes.objects.all()
        context['title'] = 'Рецепты'
        return context

    def get_queryset(self):
        queryset = super().get_queryset().all().order_by('-pk')
        test = GamesFilter(self.request.GET, queryset=queryset).qs
        print(self.request.GET)
        print(test)
        print(queryset)
        return GamesFilter(self.request.GET, queryset=queryset).qs





    # data = {
    #     'title': 'Рецепты',
    #     'recipesObjects': Recipes.objects.all(),
    #     'filtersGames': GamesFilter(request.GET,
    #                                         queryset=Recipes.objects.all().order_by(
    #                                             '-pk'))
    # }
    #
    # return render(request, 'main/all_recipes.html', data)


class recipe(DetailView):
    model = Recipes
    template_name = 'main/recipe.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context["recipe"] = Recipes.objects.get(id=self.kwargs["pk"])
        context["ingridients"] = RecipeIngredients.objects.filter(idRecipe=self.kwargs["pk"])
        context["instructions"] = Instructions.objects.filter(idRecipe=self.kwargs["pk"])
        context['grades'] = Grades.objects.all()
        context['userGrade'] = Grades.objects.filter(idRecipe=self.kwargs["pk"],idUser=self.request.user.id)
        context['favorite'] = Favorites.objects.filter(idRecipe=self.kwargs["pk"],idUser=self.request.user.id)

        star = 0
        if context['userGrade'].exists():
            for starr in context['userGrade']:
                star = starr.lvl

        favorite = 0
        if context['favorite'].exists():
            for favoritee in context['favorite']:
                favorite = 1
        # context["subsCategory"] = SubsCategory.objects.get(id=context["subs"].category)
        # context["subsServices"] = SubsServices.objects.get(id=context["subs"].service)
        # context["date"] = datetime.now().strftime('%Y-%m-%d')
        formGrades = GradesForm()
        # form = SubsForm(instance=context["subs"])
        # Измененеие цены

        # Изменение даты
        # form = form.replace("Изменяемая дата", context["date"])

        data = {
            'recipe': context['recipe'],
            'ingridients': context['ingridients'],
            'instructions': context['instructions'],
            'formGrades': formGrades,
            'userGrade': star,
            'favorite': favorite,
            'id': self.kwargs["pk"],
        }

        return data


@login_required(None, 'next', '/users/login')
def account(request):
    return render(request, 'main/account.html', {'title': 'Личный кабинет'})

def gradesAdd(request, pk):
    if request.method == 'POST':
        forms = request.POST.copy()
        gradeUser = Grades.objects.filter(idRecipe=pk,idUser=request.user.id)
        if forms.get('star') is not None:
            forms['lvl'] = 1
        if forms.get('star2') is not None:
            forms['lvl'] = 2
        if forms.get('star3') is not None:
            forms['lvl'] = 3
        if forms.get('star4') is not None:
            forms['lvl'] = 4
        if forms.get('star5') is not None:
            forms['lvl'] = 5
        if(gradeUser.exists()):
            gradeUser.delete()
        forms['idUser'] = request.user.id
        forms['idRecipe'] = pk
        request.POST = forms
        form = GradesForm(request.POST)
        if form.is_valid():
            form.save()
            allGrades = Grades.objects.filter(idRecipe=pk)
            count = 0
            gradeAll = 0
            for gradeThis in allGrades:
                count += 1
                gradeAll += gradeThis.lvl
            gradeNew = gradeAll / count
            recipe = Recipes.objects.get(id=pk)
            recipe.grade = gradeNew
            recipe.save()
        return redirect('recipe', pk)
    return render(request, 'main/index.html', {'title': 'Личный кабинет'})

def favoriteAdd(request, pk):
    if request.method == 'POST':
        forms = request.POST.copy()
        favoriteUser = Favorites.objects.filter(idRecipe=pk,idUser=request.user.id)
        if(favoriteUser.exists()):
            favoriteUser.delete()
        else:
            forms['idUser'] = request.user.id
            forms['idRecipe'] = pk
            request.POST = forms
            form = FavoritesForm(request.POST)
            if form.is_valid():
                form.save()
        return redirect('recipe', pk)
    return render(request, 'main/index.html', {'title': 'Личный кабинет'})

def favorites(request):
    recipesUser = Favorites.objects.filter(idUser=request.user.id)
    print(recipesUser)
    return render(request, 'main/favorites.html',
                  {'title': 'Любимые блюда', 'recipesUser': recipesUser}
                  )

def about(request):
    return render(request, 'main/about.html', {'title': 'О нас'})

