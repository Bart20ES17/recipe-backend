from flask import Flask, request, redirect
from recipe_api import db, app
from recipe_api.models import Recipe

@app.route('/')
def hello_world():
    """
    This way of forwarding to the main page is not the most correct.
    Rather, it should be done by optimizing the original '/' path to 
    '/recipes' automatically. However, redirection is applied due to 
    lack of time to implement the other version.
    """
    
    return redirect('/recipes')

@app.route('/recipes', methods=['POST'])
def create_recipe():
    name = request.json['name']
    rating = request.json['rating']
    favorite = request.json['favorite']
    steps = request.json['steps']
    ingredients = request.json['ingredients']
    recipe = Recipe(name, rating, favorite, steps, ingredients)
    db.session.add(recipe)
    db.session.commit()
    return format_recipe(recipe)


@app.route('/recipes', methods=['GET'])
def get_recipes():
    recipes = Recipe.query.all()
    return {'recipes': [format_recipe(recipe) for recipe in recipes]}


@app.route('/recipes/<int:id>', methods=['GET'])
def get_recipe(id):
    recipe = Recipe.query.get(id)
    return format_recipe(recipe)


@app.route('/recipes/<int:id>', methods=['PUT'])
def update_recipe(id):
    recipe = Recipe.query.get(id)
    recipe.name = request.json['name']
    recipe.ingredients = request.json['ingredients']
    recipe.favorite = request.json['favorite']
    recipe.rating = request.json['rating']
    recipe.steps = request.json['steps']
    db.session.commit()
    return format_recipe(recipe)


@app.route('/recipes/<int:id>', methods=['DELETE'])
def delete_recipe(id):
    recipe = Recipe.query.get(id)
    db.session.delete(recipe)
    db.session.commit()
    return format_recipe(recipe)


def format_recipe(recipe):
    return {
        'id': recipe.id,
        'name': recipe.name,
        'steps': recipe.steps,
        'ingredients': recipe.ingredients,
        'rating': recipe.rating,
        'favorite': recipe.favorite
    }
