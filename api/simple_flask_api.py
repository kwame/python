from flask import Flask, request, jsonify

app = Flask(__name__)

data = {"message": "Hello world!"}

@app.route('/api', methods=['GET'])
def get_data():
    return jsonify(data)

@app.route('/api', methods=['POST'])
def post_data():
    new_data = request.json
    return jsonify({"received": new_data}), 201

if __name__ == '__main__':
    app.run(debug=True)
