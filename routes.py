# from style_transfer import get_styled_image
from flask import Flask
from flask import send_file
from flask import request, session

# flask_cors.CORS(routes, expose_headers='Authorization')
import requests
from tabulate import tabulate

# import the Flask class from the flask module
from flask import Flask, Response, send_from_directory
import logging
import re 

from flask import jsonify


# from flask_cors import CORS, cross_origin



routes = Flask(__name__)

from flask import request, jsonify, render_template


import numpy as np

import os
# import logging
# from flask_cors import CORS, cross_origin


def get_news(ticker):


    url = ('http://newsapi.org/v2/everything?'
        'q=' + str(ticker) + '&'
        'from=2020-08-05&'
        'sortBy=popularity&'
        'apiKey=5092bd320d6a49509b6f0f0368b90d74') 

    response = requests.get(url)

    article_list = []

    for article in response.json()["articles"]:
        description = article["description"]
        url = article["url"]
        title = article["title"]
        date = article["publishedAt"]
        news_html = "<div class='my-4 border-bottom'><a href='" + url + "' ><h4 class='font-weight-bold my-3'>"+ title+ "</h4> </a><p class='mt-1 small'>"+ date + "</p><p class='p-2'> " + description +"</p></div>"
        article_list.append(news_html)
        

    return article_list


@routes.route("/")
def index():		 
     return render_template("index.html")

@routes.route('/<string:result>', methods=['GET'])
def get_result(result):
    news_list = get_news(result)
    return render_template('search_result.html', name = result, news = news_list)

if __name__ == "__main__":
    # routes.run(host='0.0.0.0')
 
    routes.secret_key = os.urandom(24)
    routes.run(host="0.0.0.0", use_reloader=False)



# ##############################################################
# CREATING THE SEARCH FUNCTION USING API
