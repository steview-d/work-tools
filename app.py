from flask import Flask, render_template, request, session
from bs4 import BeautifulSoup

import json
import os
import re
import requests as req

if os.path.exists('env.py'):
    import env


app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')
messages = []


@app.route('/', methods=["GET"])
def index():
    if session['variants'] is None:
        session['variants'] = []

    return render_template("index.html")


@app.route('/variant_finder', methods=["POST", "GET"])
def variant_finder():
    if request.form.get('product-url'):
        product_url = request.form['product-url']
        variants = scrape_variant(product_url)
        product_name = (
            variants['product']['variants'][0]['name'].split(' - ')[0])
        variant_list = []
        for idx, i in enumerate(variants['product']['variants']):
            variant_list.append([i])

        return render_template("variant_finder.html",
                               variants=variants['product']['variants'],
                               product_name=product_name,
                               variant_list=variant_list,
                               id_list=session['variants'])

    if request.form.get('variant_list'):
        for k, v in request.form.items():
            if k != 'variant_list':
                qqq = session['variants']
                qqq.append(v)
                session['variants'] = qqq

    if request.form.get('clear_list'):
        session['variants'] = []

    return render_template("variant_finder.html",
                           id_list=session['variants'])


def scrape_variant(url):
    try:
        r = req.get(url)
    except Exception as e:
        print(e)
        return

    # Scrape data from product page
    soup = BeautifulSoup(r.text, 'html.parser')
    result = str(soup.find(
        'script', text=re.compile('var meta = {"product":')))
    data = result.split('var meta = ')[1].split(',"page":')[0]
    json_data = json.loads(data + '}')

    return json_data


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
