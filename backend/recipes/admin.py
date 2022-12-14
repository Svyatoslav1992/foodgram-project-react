from django.contrib import admin
from users.models import Follow, User

from recipes.models import (Favourite, Ingredient, IngredientRecipe, Recipe,
                            ShoppingCart, Tag)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_unit',)
    empty_value_display = '-пусто-'
    search_fields = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'slug',)
    empty_value_display = '-пусто-'


class AmountInLine(admin.StackedInline):
    model = IngredientRecipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'text', 'image', 'cooking_time', 'author',)
    list_filter = ('author', 'tags',)
    inlines = [AmountInLine, ]


@admin.register(IngredientRecipe)
class IngredientRecipeAdmin(admin.ModelAdmin):
    list_display = ('ingredient', 'amount',)


admin.site.register(ShoppingCart)
admin.site.register(Follow)
admin.site.register(Favourite)
admin.site.register(User)
