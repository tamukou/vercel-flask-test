from flask import Flask, jsonify, requests, json

app = Flask(__name__)


@app.route("/")
def hello_world():
    return jsonify({'message': 'This is Poke API !'})


@app.route('/api/<id>', methods=["GET"])
def id(id):
    #pokeapiから取得
    name = get_name(id)

    # json_open = open('pokemon.json', 'r')
    # json_load = json.load(json_open)
    # print(json_load['section1']['key'])
    # id = id * 2
    return jsonify({'id': id, 'name': name})  


def get_name(id_str):
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

    return name

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8888, debug=True)

