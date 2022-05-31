from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('seznam/', views.RecipeListView.as_view(), name='seznam'),
    path('recept/<int:pk>', views.RecipeDetailView.as_view(),name='detail')
]