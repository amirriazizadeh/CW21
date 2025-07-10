from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Recipe(models.Model):

    Difficulty_Level = [
        ("Easy", "Easy"),
        ("Medium", "Medium"),
        ("Hard", "Hard"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    instructions = models.TextField()
    preparation_time = models.IntegerField()
    cooking_time = models.IntegerField()
    difficulty = models.CharField(max_length=10, choices=Difficulty_Level)
    categories = models.ManyToManyField(Category, related_name="recipes")

    def __str__(self) -> str:
        return self.title


class Ingredients(models.Model):
    name = models.CharField(max_length=10)
    quantity = models.CharField(max_length=100)
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="ingredients"
    )

    def __str__(self) -> str:
        return self.name
