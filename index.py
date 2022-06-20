from flask import Flask, jsonify, render_template
import urllib.request
import json
import re


app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route("/")
def index():
    html = render_template('index.html')
    return html

@app.route("/api/")
def hello_api():
    return jsonify({'message': 'This is GPA Poke API !'})

@app.route('/api/<id>', methods=["GET"])
def id(id):
    #エラー対応
    try:
        int_id = int(id)
        if int_id <= 0 or int_id >= 401:
            return jsonify({
                'error': 'Out of bounds exception', 
                'message': 'Id is out of bounds. Enter a value from 1 to 400',
                'example-url': 'https://poke-gpa-api.vercel.app/api/25'})
    except Exception as e:
        return jsonify({
            'error': 'Number format exception', 
            'message': 'Enter a value from 1 to 400',
            'example-url': 'https://poke-gpa-api.vercel.app/api/25'
            })
        
    #pokeapiから取得
    name_en = ''
    image = ''
    url = "https://pokeapi.co/api/v2/pokemon/" + id  + "/"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as res:
        body = json.load(res)
        name_en  = body['name']
        image = body['sprites']['other']['official-artwork']['front_default']

    #日本語に変換
    name_ja = ''
    json_open = open('pokemon.json', 'r')
    json_load = json.load(json_open)
    for i in json_load:
        if i['en'].lower() == name_en:
            name_ja = i['ja']

    #GPAに変換
    gpa = int(id) / 100

    return jsonify(
        gpa = gpa,
        id = int(id), 
        name_ja = name_ja,
        name_en = name_en,
        image_url = image
    )  

