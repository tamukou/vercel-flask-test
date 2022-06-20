from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return jsonify({'message': 'This is Poke API !'})


@app.route('/api/<id>', methods=["GET"])
def id(id):
    id = id * 2
    return jsonify({'id': id})  


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8888, debug=True)

