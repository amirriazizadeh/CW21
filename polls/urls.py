from django.urls import path
from . import views

urlpatterns = [
    path("category-form/", views.CategoryView, name="category"),
    path("recipe-form/", views.RecipeView, name="recipe"),
    path("ingredients-form/", views.IngredientsView, name="ingredients"),
    path("recipe-list/", views.RecipelistView, name="recipe_list"),
    path("recipe-details/<int:pk>", views.RecipeDetailsView, name="recipe_integrate"),
    path("recipe-update/<int:pk>", views.RecipeUpdateView, name="recipe_update"),
    path("recipe-delete/<int:pk>", views.RecipeDeleteView, name="confirm"),
]
