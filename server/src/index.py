"""
Server File
- Handles Entering and Exiting of the Backend
"""

from flask import Flask, render_template,request
from services import get_news, get_fin_data

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('mainpage.html')

@app.route('/info/<country>')
def get_info(country):
	location=country
	news_data = get_news(str(location))
	news=[]
	for i in news_data:
		newsinfo={'source':i[0],'title':i[1],'link':i[2],'detail':i[3]}
		news.append(newsinfo)
	fin_data = get_fin_data(str(location))

	return render_template('news.html', post=[news, fin_data])
	
if __name__ == '__main__':
	app.run(debug=True)

   