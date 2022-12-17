from recipe_api.models import Recipe
import pytest

def test_create_recipe():
    """
    CHANGE THIS DESCRIPTION!

    GIVEN a Account model
    WHEN a new Recipe is created
    THEN check the name, steps, rating, ingredients, favorite fields are defined correctly
    """
    recipe = Recipe('Test Recipe', 2, True, 'No steps available', 'Carrot, Apple, Butter')
    assert recipe.name == 'Test Recipe'
    assert recipe.steps == 'No steps available'
    assert recipe.rating == 2
    assert recipe.ingredients == 'Carrot, Apple, Butter'
    assert recipe.favorite == True

