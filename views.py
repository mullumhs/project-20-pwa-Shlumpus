from flask import render_template, request, redirect, url_for, flash
from models import db,Book # Also import your database model here

# Define your routes inside the 'init_routes' function
# Feel free to rename the routes and functions as you see fit
# You may need to use multiple methods such as POST and GET for each route
# You can use render_template or redirect as appropriate
# You can also use flash for displaying status messages

def init_routes(app):

    @app.route('/', methods=['GET'])
    def get_items():
        # This route should retrieve all items from the database and display them on the page.
        return render_template('index.html', message='Displaying all items')



    @app.route('/add', methods=['GET', 'POST'])
    def add_item():
        if request.method == 'POST':
            new_book = Book(
                title=request.form['title'],
                author=request.form['author'],
                year=int(request.form['year']),
                rating=float(request.form['rating']),
                genre=request.form['genre'],
                description=request.form['description'],
                image_url=request.form['image']
            )

            db.session.add(new_book)
            db.session.commit()
            return redirect(url_for('index'))

        else:
            return render_template('add_item.html')

    @app.route('/update', methods=['POST'])
    def update_item():
        # This route should handle updating an existing item identified by the given ID.
        return render_template('index.html', message=f'Item updated successfully')


    @app.route('/delete', methods=['GET'])
    def delete_item():

        id=request.args.get('id')
        item = Book.query.get(id)
        db.session.delete(item)
        db.session.commit()
        
        # This route should handle deleting an existing item identified by the given ID.
        return render_template('index.html', message=f'Item deleted successfully')