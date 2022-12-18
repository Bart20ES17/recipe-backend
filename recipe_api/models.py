from recipe_api import db


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    steps = db.Column(db.String(1000), nullable=False)
    rating = db.Column(db.Integer, nullable=False, default=0)
    ingredients = db.Column(db.String(40), nullable=False, default="None")
    favorite = db.Column(db.Boolean(), nullable=False, default=False)

    def __repr__(self):
        return '<Task %r>' % self.id  

    def __init__(self, name, rating, favorite, steps, ingredients):
        self.name = name
        self.steps = steps
        self.rating = rating
        self.ingredients = ingredients
        self.favorite = favorite
