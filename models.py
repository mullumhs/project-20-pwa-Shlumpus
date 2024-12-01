from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    genre = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.String, nullable=False)
    

# Define your database model here
# Example: class Item(db.Model):