from flask import render_template
from app import app

from .request import get_news

@app.route('/general')
def general():
	'''
	View root page function that returns the index page and its data
	'''
	# Getting popular news
	general_news = get_news('general')
	title = 'Home Page - Get The latest News Online Across The World'
	return render_template('general.html',title = title,general=general_news)

# @app.route('/newsArticle')
# def newsArticle():
#
#     return render_template('newsArticle.html')
#
# @app.route('/newsSource')
# def newsSource():
#
#     return render_template('newsSource.html')
