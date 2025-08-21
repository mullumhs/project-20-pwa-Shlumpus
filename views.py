from flask import Flask
from flask import render_template, request, redirect, url_for, flash
from models import db, Track # Also import your database model here

# Define your routes inside the 'init_routes' function
# Feel free to rename the routes and functions as you see fit
# You may need to use multiple methods such as POST and GET for each route
# You can use render_template or redirect as appropriate
# You can also use flash for displaying status messages

def init_routes(app):

    @app.route('/', methods=['GET'])
    def index():
        # This route should retrieve all items from the database and display them on the page.
        tracks = Track.query.all()
        return render_template('index.html', tracks=tracks)

    @app.route('/add', methods=['GET', 'POST'])
    def add_item():
        if request.method == 'POST':
            new_track = Track(
                title=request.form['title'],
                producer=request.form['producer'],
                date=str(request.form['date']),
                bpm=int(request.form['bpm']),
                key=str(request.form['key']),
                genre=request.form['genre'],
                mood=request.form['mood'],
                description=request.form['description'],
                image=request.form['image']
            )

            db.session.add(new_track)
            db.session.commit()
            return redirect(url_for('index'))

        else:
            return render_template('add_item.html')

    @app.route('/edit', methods=['POST'])
    def edit_item():
        # This route should handle updating an existing item identified by the given ID.
        if request.method == 'POST':
            id = request.form['id']
            track=Track.query.get_or_404(id)
            track.title=request.form['title']
            track.producer=request.form['producer']
            track.date=str(request.form['date'])
            track.bpm=int(request.form['bpm'])
            track.key=str(request.form['key'])
            track.genre=request.form['genre']
            track.mood=request.form['mood']
            track.description=request.form['description']
            track.image=request.form['image']  
            db.session.commit()
            return redirect(url_for('edit_item'))
        else:        
            id = request.args.get('id')
            track=Track.query.get_or_404(id)
            return render_template('edit_item.html', track=track)

    @app.route('/info', methods=['GET', 'POST'])
    def display_info():
        if request.method == 'GET':
            id=request.args.get('id')
            track = Track.query.get(id) 
            print(id)
            return render_template('info.html', track=track)
        else:
            return render_template('add_item.html')

    @app.route('/delete', methods=['GET'])
    def delete_item():
        id=request.args.get('id')
        track = Track.query.get(id)
        db.session.delete(track)
        db.session.commit()
        
        # This route should handle deleting an existing item identified by the given ID.
        return redirect(url_for('index'))