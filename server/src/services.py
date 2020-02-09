"""
Services File
- Handles GET requests and Data Transformation
"""
import os
import pandas as pd
from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='b1d0aa01a278480a8ad685eb161edcba')

def get_news(country):
    data = newsapi.get_top_headlines(category='business', country=country, page_size=5,language='en')
    extracted_data = []
    for articles in data['articles']:
        source = articles['source']['name']
        title = articles['title']
        url = articles['url']
        description = articles['description']
        extracted_data.append([source, title, url, description])
    return extracted_data

def get_fin_data(country):
    path = os.getcwd()
    df = pd.read_csv(path + f"/server/src/csv/{country}.csv", header=1)
    df = df.rename(columns={"Unnamed: 0": "Date"})
    date_array = df['Date'].to_list()
    high_array = df['high'].to_list()
    low_array = df['low'].to_list()
    open_array = df['open'].to_list()
    last_price_array = df['last_price'].to_list()
    mid_average_point_array = [(val + last_price_array[idx])/2 for idx, val in enumerate(open_array)]
    data_array = []
    for index, value in enumerate(date_array):
        data_array.append([value, low_array[index], open_array[index], last_price_array[index], high_array[index], mid_average_point_array[index]])

    print(data_array)
    return data_array
