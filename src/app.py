from flask import Flask, flash, redirect, render_template, request, session, abort
from models import db, DB_URL

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silence the deprecation warning

db.init_app(app)

@app.route("/")
def index():
    return "Hello, World!"
 
@app.route("/<string:name>/")
def getName(name):
    return render_template('test.html', name=name)

@app.cli.command('resetdb')
def resetdb_command():
    """Destroys and re-creates the database and all its tables."""

    from sqlalchemy_utils import database_exists, create_database, drop_database
    if database_exists(DB_URL):
        print('Deleting database...')
        drop_database(DB_URL)
    if not database_exists(DB_URL):
        print('Creating database...')
        create_database(DB_URL)

    print('Creating tables...')
    db.create_all()
    print('Complete!')
 
if __name__ == "__main__":
    app.run()