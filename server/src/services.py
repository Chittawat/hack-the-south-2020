"""
Services File
- Handles GET requests and Data Transformation
"""
from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='b1d0aa01a278480a8ad685eb161edcba')

def get_news(country):
    data = newsapi.get_top_headlines(category='general', country=country, page_size=5)
    extracted_data = []
    for articles in data['articles']:
        source = articles['source']['name']
        title = articles['title']
        url = articles['url']
        description = articles['description']
        extracted_data.append([source, title, url, description])
    return extracted_data
