from flask import render_template
from app import app


@app.route('/')
def index():


    title = 'Home - Welcome to your number one news site'
    return render_template('index.html', title = title)

@app.route('/newsArticle')
def newsArticle():

    return render_template('newsArticle.html')

@app.route('/newsSource')
def newsSource():

    return render_template('newsSource.html')
