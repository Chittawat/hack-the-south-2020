"""
Server File
- Handles Entering and Exiting of the Backend
"""
import numpy as np
from statistics import mean
from flask import Flask, render_template,request
from services import get_news, get_fin_data, get_predictions

app = Flask(__name__)



@app.route('/')
def index():
	ca_data = get_fin_data(str('ca'))
	gb_data = get_fin_data(str('gb'))
	jp_data = get_fin_data(str('jp'))
	us_data = get_fin_data(str('us'))
	nz_data = get_fin_data(str('nz'))
	au_data = get_fin_data(str('au'))
	ch_data = get_fin_data(str('ch'))
	
	clist=[{'country':'ca','conversion':'USD/CAD','Price':float(ca_data[-1][3]),'PriceInv':'{0:.4f}'.format(1/float(ca_data[-1][3])),'PChange':'{0:.4f}'.format((float(ca_data[-2][3]) - float(ca_data[-1][3]))/float(ca_data[-2][-3]) * 100),'PMP24H':'{0:.4f}'.format(float((ca_data[-1][-1]))),'PMP5D':'{0:.4f}'.format(mean([float(ca_data[-i][-1]) for i in range(1, 6)])),'PMP1M':'{0:.4f}'.format(mean([float(ca_data[-i][-1]) for i in range(1, 31)])),'PGph':[['Date','Value'],[1/1/2019,20],[2/1/2019,40],[3/1/2019,10]]},
	{'country':'gb','conversion':'GBP/USD','Price':float(gb_data[-1][3]),'PriceInv':'{0:.4f}'.format(1/float(gb_data[-1][3])),'PChange':'{0:.4f}'.format((float(gb_data[-2][3]) - float(gb_data[-1][3]))/float(gb_data[-2][-3]) * 100),'PMP24H':'{0:.4f}'.format(float((gb_data[-1][-1]))),'PMP5D':'{0:.4f}'.format(mean([float(gb_data[-i][-1]) for i in range(1, 6)])),'PMP1M':'{0:.4f}'.format(mean([float(gb_data[-i][-1]) for i in range(1, 31)])),'PGph':[['Date','Value'],[1/1/2019,20],[2/1/2019,40],[3/1/2019,10]]},
	{'country':'jp','conversion':'USD/JPY','Price':float(jp_data[-1][3]),'PriceInv':'{0:.4f}'.format(1/float(jp_data[-1][3])),'PChange':'{0:.4f}'.format((float(jp_data[-2][3]) - float(jp_data[-1][3]))/float(jp_data[-2][-3]) * 100),'PMP24H':'{0:.2f}'.format(float((jp_data[-1][-1]))),'PMP5D':'{0:.2f}'.format(mean([float(jp_data[-i][-1]) for i in range(1, 6)])),'PMP1M':'{0:.2f}'.format(mean([float(jp_data[-i][-1]) for i in range(1, 31)])),'PGph':[['Date','Value'],[1/1/2019,20],[2/1/2019,40],[3/1/2019,10]]},
	{'country':'au','conversion':'AUD/USD','Price':float(au_data[-1][3]),'PriceInv':'{0:.4f}'.format(1/float(au_data[-1][3])),'PChange':'{0:.4f}'.format((float(au_data[-2][3]) - float(au_data[-1][3]))/float(au_data[-2][-3]) * 100),'PMP24H':'{0:.4f}'.format(float((au_data[-1][-1]))),'PMP5D':'{0:.4f}'.format(mean([float(au_data[-i][-1]) for i in range(1, 6)])),'PMP1M':'{0:.4f}'.format(mean([float(au_data[-i][-1]) for i in range(1, 31)])),'PGph':[['Date','Value'],[1/1/2019,20],[2/1/2019,40],[3/1/2019,10]]},
	{'country':'nz','conversion':'NZD/USD','Price':float(nz_data[-1][3]),'PriceInv':'{0:.4f}'.format(1/float(nz_data[-1][3])),'PChange':'{0:.4f}'.format((float(nz_data[-2][3]) - float(nz_data[-1][3]))/float(nz_data[-2][-3]) * 100),'PMP24H':'{0:.4f}'.format(float((nz_data[-1][-1]))),'PMP5D':'{0:.4f}'.format(mean([float(nz_data[-i][-1]) for i in range(1, 6)])),'PMP1M':'{0:.4f}'.format(mean([float(nz_data[-i][-1]) for i in range(1, 31)])),'PGph':[['Date','Value'],[1/1/2019,20],[2/1/2019,40],[3/1/2019,10]]},
	{'country':'ch','conversion':'USD/CHF','Price':float(ch_data[-1][3]),'PriceInv':'{0:.4f}'.format(1/float(ch_data[-1][3])),'PChange':'{0:.4f}'.format((float(ch_data[-2][3]) - float(ch_data[-1][3]))/float(ch_data[-2][-3]) * 100),'PMP24H':'{0:.4f}'.format(float((ch_data[-1][-1]))),'PMP5D':'{0:.4f}'.format(mean([float(ch_data[-i][-1]) for i in range(1, 6)])),'PMP1M':'{0:.4f}'.format(mean([float(ch_data[-i][-1]) for i in range(1, 31)])),'PGph':[['Date','Value'],[1/1/2019,20],[2/1/2019,40],[3/1/2019,10]]},
	{'country':'us','conversion':'EUR/USD','Price':float(us_data[-1][3]),'PriceInv':'{0:.4f}'.format(1/float(us_data[-1][3])),'PChange':'{0:.4f}'.format((float(us_data[-2][3]) - float(us_data[-1][3]))/float(us_data[-2][-3]) * 100),'PMP24H':'{0:.4f}'.format(float((us_data[-1][-1]))),'PMP5D':'{0:.4f}'.format(mean([float(us_data[-i][-1]) for i in range(1, 6)])),'PMP1M':'{0:.4f}'.format(mean([float(us_data[-i][-1]) for i in range(1, 31)])),'PGph':[['Date','Value'],[1/1/2019,20],[2/1/2019,40],[3/1/2019,10]]}
	]	
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

@app.route('/about')
def get_about():
	render_template('about.html')
	
if __name__ == '__main__':
	app.run(debug=True)

   