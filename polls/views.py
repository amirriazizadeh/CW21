from django.shortcuts import render,get_object_or_404,redirect
from .forms import CategoryForm, RecipeForm, IngredientsForm
from .models import Recipe

# insert
# ===========================================================================
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
# ==========================================================================================




# list View 
# ==========================================================================================

def RecipelistView(request):
    recipelist = Recipe.objects.all()
    return render(request , 'recipeList.html',{'recipe':recipelist})





def RecipeDetailsView(request,pk):
    rsp=Recipe.objects.get(pk=pk)
    # intg=rsp.ingredients.all()
    # intg = get_object_or_404( Recipe.objects.prefetch_related('ingredients', 'categories') , pk=pk)
    return render(request, 'recipe_detail.html', {'rsp': rsp})

def RecipeUpdateView(request,pk):
    old=Recipe.objects.get(pk=pk)
    form_old = RecipeForm(instance=old)
    if request.method == "GET":
        return render(request,'recipe_update.html',{'rsp':form_old})
    elif request.method == "POST":
        rsp = Recipe.objects.all()
        new = RecipeForm(request.POST,instance=old)
        if new.is_valid():
            new.save()
            return redirect('recipe_list')

def RecipeDeleteView(request,pk):
    rsp = Recipe.objects.get(pk=pk)
    if request.method == "GET":
        return render(request,'confirm.html',{'rsp':rsp})
    elif request.method == "POST":
        rsp.delete()
        return redirect('recipe_list')
    
