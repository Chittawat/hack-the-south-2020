"""
Server File
- Handles Entering and Exiting of the Backend
"""

from flask import Flask, render_template
from services import get_news

app = Flask(__name__)

@app.route('/')

@app.route('/info')
def news(country):
    news_data = get_news(country)
    return render.template('../../webpage/news.html', posts=news_data)


   