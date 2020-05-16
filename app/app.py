from flask import Flask
from flask import render_template
import requests
import json
from flask import abort

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello!!!!!! Deutsche Börse Group'

@app.route('/jokes')
def jokes():
    url = 'https://api.chucknorris.io/jokes/random'
    r = requests.get(url)
    data= r.json()
    return render_template("jokes.html", title='Joke Page', all_items=data)
 

@app.route('/categories/<category>')
def categories(category):
    url = 'https://api.chucknorris.io/jokes/categories'
    r = requests.get(url)
    if category in r.text:
     out_url = 'https://api.chucknorris.io/jokes/random?category={}'.format(category)
     response = requests.get(out_url)
     categ_data = response.json()
    else:
     return abort(404, 'Category  {} searching for does not exist'.format(category))
    return render_template("category.html", title='Category Page', all_items=categ_data)
     

@app.route('/query/<query>')
def query(query):
    url = 'https://api.chucknorris.io/jokes/categories'
    r = requests.get(url)
    if query in r.text:
     query_url = 'https://api.chucknorris.io/jokes/search?query={}'.format(query)
     response = requests.get(query_url)
     query_data = response.json()
    else:
     return abort(404, 'Category  {} searching for does not exist'.format(query))
    return render_template("query.html", title='Category Page', all_items=query_data, query=query)



if __name__ == '__main__':
  app.run()
