from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('seznam/', views.RecipeListView.as_view(), name='seznam'),
    path('Recipe/<int:id>', views.RecipeDetailView.as_view(),name='recept-detail')
]