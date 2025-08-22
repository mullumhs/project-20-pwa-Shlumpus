from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Track(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    producer = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String, nullable=False)
    bpm = db.Column(db.Integer, nullable=False)
    key = db.Column(db.String, nullable=False)
    genre = db.Column(db.String(100), nullable=False)
    mood = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=False)
    audio_file = db.Column(db.String, nullable=False)

# Define your database model here
# Example: class Item(db.Model):