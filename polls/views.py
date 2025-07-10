from django.shortcuts import render
from .forms import CategoryForm, RecipeForm, IngredientsForm


def CategoryView(request):

    if request.method == "GET":
        categoryForm = CategoryForm()
        return render(request, "Category.html", {"category": categoryForm})
    elif request.method == "POST":
        categoryFormFilled = CategoryForm(request.POST)
        if categoryFormFilled.is_valid():
            categoryFormFilled.save()
            msg = "Category Added Successfully"
            return render(
                request,
                "Category.html",
                {"msg": msg, "category": categoryFormFilled},
            )


def RecipeView(request):

    if request.method == "GET":
        recipeForm = RecipeForm()
        return render(request, "Recipe.html", {"recipe": recipeForm})
    elif request.method == "POST":
        recipeFormFilled = RecipeForm(request.POST)
        if recipeFormFilled.is_valid():
            recipeFormFilled.save()
            msg = "Recipe Added Successfully"
            return render(
                request,
                "Recipe.html",
                {"msg": msg, "recipe": recipeFormFilled},
            )


def IngredientsView(request):

    if request.method == "GET":
        ingredientForm = IngredientsForm()
        return render(request, "Ingredient.html", {"ingredient": ingredientForm})
    elif request.method == "POST":
        ingredientsFormFilled = IngredientsForm(request.POST)
        if ingredientsFormFilled.is_valid():
            ingredientsFormFilled.save()
            msg = "Ingredient Added Successfully"
            return render(
                request,
                "Ingredient.html",
                {"msg": msg, "ingredient": ingredientsFormFilled},
            )
