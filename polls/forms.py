from django.forms import ModelForm
from .models import Category, Recipe, Ingredients


class CategoryForm(ModelForm):

    class Meta:
        model = Category
        fields = "__all__"


class RecipeForm(ModelForm):

    class Meta:
        model = Recipe
        fields = "__all__"

    


class IngredientsForm(ModelForm):

    class Meta:
        model = Ingredients
        fields = "__all__"
