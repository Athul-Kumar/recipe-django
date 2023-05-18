from django.urls import path
from RecipeProject import views

urlpatterns = [
    
    path('', views.Create_recipe, name="recipe-page"),
    path('recipe-list/', views.Recipe_list, name="recipe-list"),
    path('recipe-list/recipe-delete/<id>/', views.Recipe_delete, name="recipe-delete"),
    path('recipe-list/recipe-update/<id>/', views.Recipe_update, name="recipe-update")
   
]