import pytest
from recipe_api.models import Recipe
from recipe_api import db, app


@pytest.fixture
def testing_client(scope='module'):
    db.create_all()
    recipe = Recipe('Test Recipe', 'No steps available', 2, 'Carrot, Apple, Butter', True)
    db.session.add(recipe)
    db.session.commit()

    with app.test_client() as testing_client:
        yield testing_client

    db.drop_all()
