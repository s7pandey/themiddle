from flask import Flask, render_template, request, redirect, url_for
import requests
import config
import json

app = Flask(__name__, static_url_path='')

apiKey = "&apiKey=" + config.news_api['key']
newsApiEverythingUrl = "http://beta.newsapi.org/v2/everything?language=en&"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/everthingData')
def get_index_data(page):
    # sources = ['breitbart-news', 'cnn', 'the-new-york-times'] # for final release - request.args.getlist('sources')
    response = requests.get(newsApiEverythingUrl + "sources=breitbart-news, cnn, the-new-york-times&page="+ str(page) + apiKey)
    return json.loads(response.text)


everythingData = {}
i = 1
while(i < 1000):
    everythingData[i] = get_index_data(i)
    i += 1


with open('list_of_articles.json', 'w') as out_file:
    json.dump(everythingData,out_file)