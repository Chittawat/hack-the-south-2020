"""
Services File
- Handles GET requests and Data Transformation
"""
import os
import pandas as pd
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import TimeseriesGenerator 
from sklearn.preprocessing import MinMaxScaler
import numpy as np
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
    df = pd.read_csv(path + f"/csv/{country}.csv", header=1)
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

    return data_array

def get_predictions(country_array):
    n_input = 30
    # change to numpy array for ease of access
    # index 0 = date, index 1 = mid point
    data = np.array(country_array)[:, 5]
    train_data = data[:11000].reshape(11000, 1)
    # path of model file
    model_path = os.path.abspath('model/gbp_usd.h5')
    model = tf.keras.models.load_model(model_path)
    scaler = MinMaxScaler()
    smoothing_window_size = 2500
    for di in range(0,10000,smoothing_window_size):
        scaler.fit(train_data[di:di+smoothing_window_size,:])
        train_data[di:di+smoothing_window_size,:] = scaler.transform(train_data[di:di+smoothing_window_size,:])
    
    test_data = train_data[-n_input:]
    test_generator = TimeseriesGenerator(test_data, test_data, length=30, batch_size=1)
    

    return 'test' #list

get_predictions(get_fin_data('gb'))