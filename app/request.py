from app import app
import urllib.request,json
from .models import newsSource

NewsSource = newsSource.NewsSource

api_key = app.config['NEWS_API_KEY']
base_url = app.config["NEWS_API_BASE_URL"]
