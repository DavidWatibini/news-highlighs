from flask import render_template
from app import app


@app.route('/')
def index():

    return render_template('index.html')

@app.route('/newsArticle')
def newsArticle():

    return render_template('newsArticle.html')

@app.route('/newsSource')
def newsSource():

    return render_template('newsSource.html')
