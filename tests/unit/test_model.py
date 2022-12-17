from recipe_api.models import Recipe
import pytest

def test_create_account():
    """
    CHANGE THIS DESCRIPTION!

    GIVEN a Account model
    WHEN a new Account is created
    THEN check the name, account_number, balance, currency, status and created_at fields are defined correctly
    """
    recipe = Recipe('Cake', 'No steps available', 2, 'Carrot, Apple, Butter', True)
    assert recipe.name == 'Cake'
    assert recipe.steps == '€'
    assert recipe.rating == 2
    assert recipe.ingredients == 'Carrot, Apple, Butter'
    assert recipe.favorite == True

