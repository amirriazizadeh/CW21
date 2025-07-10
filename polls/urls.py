from django.urls import path
from . import views

urlpatterns = [
    path("category-form/", views.CategoryView, name="category"),  # type: ignore
    path("recipe-form/", views.RecipeView, name="recipe"),  # type: ignore
    path("ingredients-form/", views.IngredientsView, name="ingredients"),  # type: ignore
]
