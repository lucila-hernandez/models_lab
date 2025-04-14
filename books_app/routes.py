"""Import packages and modules."""
import os
from flask import Blueprint, request, render_template, redirect, url_for, flash
from datetime import date, datetime
from books_app.models import Book, Author, Genre
from books_app.models import User


# Import app and db from events_app package so that we can run app
from books_app import app, db

main = Blueprint("main", __name__)

##########################################
#           Routes                       #
##########################################

@main.route('/')
def homepage():
    users = User.query.all()
    return render_template('home.html')

@main.route('/profile/<username>')
def profile(username):
    user = User.query.filter_by(username=username).first()
    book = user.favorite_books[0]
    return render_template('profile.html', username=username, book=book)
