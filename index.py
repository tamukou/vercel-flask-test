from flask import Flask, jsonify, render_template
import requests
import json
import re


app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


# @app.route("/")
# def index():
#     html = render_template('index.html')
#     return html

@app.route("/api/")
def hello_api():
    return jsonify({'message': 'This is Poke API !'})

@app.route('/api/<id>', methods=["GET"])
def id(id):
    #エラー対応
    try:
        int_id = int(id)
        if int_id <= 0 or int_id >= 401:
            return jsonify({
                'error': 'Out of bounds exception', 
                'message': 'Id is out of bounds. Enter a value from 1 to 400',
                'example-url': 'https://poke-api-ja.vercel.app/api/25'})
    except Exception as e:
        return jsonify({
            'error': 'Number format exception', 
            'message': 'Enter a value from 1 to 400',
            'example-url': 'https://poke-api-ja.vercel.app/api/25'
            })
        
    #pokeapiから取得
    url = "https://pokeapi.co/api/v2/pokemon/" + id  + "/"
    r = requests.get(url, timeout=5)
    r = r.json()
    name_en  = r['name']
    image = r['sprites']['other']['official-artwork']['front_default']

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
        image = image
    )  


def get_name_image(id_str):
    url = "https://pokeapi.co/api/v2/pokemon/" + id_str  + "/"
    r = requests.get(url, timeout=5)
    r = r.json()
    name  = r['name']
    id    = r['id']
    image = r['sprites']['front_default']
    types = r['types'][0]['type']['name']

    print(id)
    print(name)
    print(image)
    print(types)

    return name, image

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8888, debug=True)

