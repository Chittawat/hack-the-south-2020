"""
Server File
- Handles Entering and Exiting of the Backend
"""

from flask import Flask, render_template,request
from services import get_news, get_fin_data, get_predictions

app = Flask(__name__)

clist=[{'country':'ca','conversion':'USD/CAD','Price':0,'PriceInv':0,'PChange':0,'PMP24H':0,'PMP5D':0,'PMP1M':0,'PGph':[['Date','Value'],[1/1/2019,20],[2/1/2019,40],[3/1/2019,10]]},
	{'country':'gb','conversion':'GBP/USD','Price':0,'PriceInv':0,'PChange':0,'PMP24H':0,'PMP5D':0,'PMP1M':0,'PGph':[['Date','Value'],[1/1/2019,20],[2/1/2019,40],[3/1/2019,10]]},
	{'country':'jp','conversion':'USD/JPY','Price':0,'PriceInv':0,'PChange':0,'PMP24H':0,'PMP5D':0,'PMP1M':0,'PGph':[['Date','Value'],[1/1/2019,20],[2/1/2019,40],[3/1/2019,10]]},
	{'country':'au','conversion':'AUD/USD','Price':0,'PriceInv':0,'PChange':0,'PMP24H':0,'PMP5D':0,'PMP1M':0,'PGph':[['Date','Value'],[1/1/2019,20],[2/1/2019,40],[3/1/2019,10]]},
	{'country':'nz','conversion':'NZD/USD','Price':0,'PriceInv':0,'PChange':0,'PMP24H':0,'PMP5D':0,'PMP1M':0,'PGph':[['Date','Value'],[1/1/2019,20],[2/1/2019,40],[3/1/2019,10]]},
	{'country':'ch','conversion':'USD/CHF','Price':0,'PriceInv':0,'PChange':0,'PMP24H':0,'PMP5D':0,'PMP1M':0,'PGph':[['Date','Value'],[1/1/2019,20],[2/1/2019,40],[3/1/2019,10]]},
	{'country':'us','conversion':'EUR/USD','Price':0,'PriceInv':0,'PChange':0,'PMP24H':0,'PMP5D':0,'PMP1M':0,'PGph':[['Date','Value'],[1/1/2019,20],[2/1/2019,40],[3/1/2019,10]]}
	]	

@app.route('/')
def index():
	return render_template('mainpage.html',clist=clist)

@app.route('/info/<country>')
def get_info(country):
	location=country
	news_data = get_news(str(location))
	news=[]
	for i in news_data:
		newsinfo={'source':i[0],'title':i[1],'link':i[2],'detail':i[3]}
		news.append(newsinfo)
	fin_data = get_fin_data(str(location))

	predictions = get_predictions(fin_data, country)

	return render_template('news.html', post=[news, fin_data, predictions])
	
if __name__ == '__main__':
	app.run(debug=True)

   