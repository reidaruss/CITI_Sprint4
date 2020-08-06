import requests
from tabulate import tabulate

# import the Flask class from the flask module
from flask import Flask, Response, send_from_directory
import logging
import re 

# ##############################################################
# CREATING THE SEARCH FUNCTION USING API

print("What would you like to search?")
user_input=input()


url = ('http://newsapi.org/v2/everything?'
       'q=' + str(user_input) + '&'
       'from=2020-08-05&'
       'sortBy=popularity&'
       'apiKey=5092bd320d6a49509b6f0f0368b90d74') 

response = requests.get(url)

#print(response.json())

description = " "
url= " "
title = " "
date = " "
article_list = []

for article in response.json()["articles"]:
    description = article["description"]
    url = article["url"]
    title = article["title"]
    date = article["publishedAt"]
    article_list.append([title,date,url,description])
    

print(article_list)

# ##############################################################
# CREATING THE HTML FILE


f = open('news.html','w')
html_code = """
<!DOCTYPE html>
<html>
<body>
<style>
body {
	background-color:#FFFFFF;
}
</style>
<h3 align=center> YOUR CHOSEN ARTICLES </h3>
<!-- ARTICLES HERE -->
</body>
</html>
"""

html_code = html_code.replace("<!-- ARTICLES HERE -->", tabulate(article_list, tablefmt='html'))


# ##############################################################
# CREATING THE WEBSITE

# create the application object
app = Flask(__name__, static_url_path='', static_folder='./')

# use decorators to link the function to a url
@app.route('/')
def homepage():
    # return app.send_static_file('recipes.html')

    content = html_code
    content = re.sub(r'[^\x00-\x7F]+',' ', content)

    return Response(content, "text/html")

app.run(debug = True, use_reloader=False)