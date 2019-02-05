from flask import render_template
from app import app

from .request import get_news,get_article

@app.route('/general')
def general():
	'''
	View root page function that returns the index page and its data
	'''
	# Getting popular news
	general_news = get_news('general')
	title = 'general-news Page - Get The latest News Online'
	return render_template('general.html',title = title,general=general_news)

@app.route('/')
def index():

    news_article = get_article('article')
    title = 'Home Page - Get The latest News Online'
    return render_template('index.html',title = title, article=news_article)

# @app.route('/newsSource')
# def newsSource():
#
#     return render_template('newsSource.html')
