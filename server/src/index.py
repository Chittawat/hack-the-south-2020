"""
Server File
- Handles Entering and Exiting of the Backend
"""

from flask import Flask
from services import get_news

app = Flask(__name__)

@app.route('/')

@app.route('/info')
def news(country):
    news_data = get_news(country)
    return render.template('index.html', posts=news_data)


   