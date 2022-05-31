from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Recipe

# Create your views here.
def index(request):
    num_recipe = Recipe.objects.all().count()
    recepty = Recipe.objects.all()
    context = {
        'num_recipe':num_recipe,
        'title': 'KalorickyWeb',
        'recepty': recepty
    }
    return render(request, 'index.html', context=context)

class RecipeListView(ListView):
    model = Recipe
    template_name = 'list.html'
    context_object_name = 'recepty'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'detail.html'
    context_object_name = 'detailReceptu'