# Write tests for al routes
from recipe_api import app
import pytest


def test_get_recipes(testing_client):
    
    response = testing_client.get('/recipes')
    assert response.status_code == 200


def test_dummy_wrong_path():
    
    with app.test_client() as client:
        response = client.get('/wrong_path')
        assert response.status_code == 404


def test_create_recipe(testing_client):
    
    response = testing_client.post(
        '/recipes', json={'name': 'Cake', 'ingredients': 'Carrot, Banana', "steps": "Mix all ingredients", "rating": 5, "favorite": True})
    assert response.status_code == 200
    assert response.json['name'] == 'Cake'
    assert response.json['ingredients'] == 'Carrot, Banana'
    assert response.json['steps'] == 'Mix all ingredients'
    assert response.json['rating'] == 5
    assert response.json['favorite'] == True
    

def test_delete_recipe(testing_client):
    response = testing_client.delete('/recipes/1')
    assert response.status_code == 200


def test_update_recipe(testing_client):

    update = testing_client.put(
        '/recipes/1', json={'name': 'Ice-Cream', 'ingredients': 'Milk, Chocolate', "steps": "Freeze all ingredients", "rating": 3, "favorite": False})
    assert update.status_code == 200
    assert update.json['name'] == 'Ice-Cream'
    assert update.json['ingredients'] == 'Milk, Chocolate'
    assert update.json['steps'] == 'Freeze all ingredients'
    assert update.json['rating'] == 3
    assert update.json['favorite'] == False


def get_recipe(testing_client):
    response = testing_client.get('/recipes/1')
    assert response.status_code == 200
    assert response.json['name'] == 'Ice-Cream'
    assert response.json['ingredients'] == 'Milk, Chocolate'
    assert response.json['steps'] == 'Freeze all ingredients'
    assert response.json['rating'] == 3
    assert response.json['favorite'] == False



