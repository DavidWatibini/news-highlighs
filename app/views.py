from flask import render_template
from app import app


@app.route('/')
def index():

    return render_template('index.html')

@app.route('/news-article')
def index():

    return render_template('news-article.html')

@app.route('/news-source')
def index():

    return render_template('news-source.html')
