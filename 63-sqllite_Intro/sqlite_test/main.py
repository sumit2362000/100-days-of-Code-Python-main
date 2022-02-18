
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# import sqlite3
'''Create a connection to a new database'''
# db = sqlite3.connect("Books-collection.db")
'''Create a cursor which will control the database'''
# cursor = db.cursor()
'''Create a table
https://www.w3schools.com/sql/sql_ref_create_table.asp
created new table and labeled it as 'books'
id INTEGER PRIMARY KEY - First field, called "id" of data type INTEGER and it will be the PRIMARY KEY for this table.
title varchar(250) NOT NULL UNIQUE - Field called "title" and it accepts a variable-length string composed of characters. 
    The 250 in brackets is the maximum length of the text. 
    NOT NULL means it must have a value and cannot be left empty. 
    UNIQUE means no two records in this table can have the same title.
author varchar(250) NOT NULL -  A field that accepts variable-length Strings up to 250 characters called author that cannot be left empty.
rating FLOAT NOT NULL -  A field that accepts FLOAT data type numbers, cannot be empty and the field is called rating.
'''
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
'''Adding data to book table'''
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()


'''
https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/
https://pythonbasics.org/flask-sqlalchemy/
'''
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
#Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

'''Create Table'''
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    #Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'

db.create_all()

'''Create Record'''
new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
db.session.add(new_book)
db.session.commit()
