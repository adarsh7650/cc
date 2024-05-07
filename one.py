from flask import Flask, jsonify, request

app = Flask(__name__)
numbers = []

@app.route('/numbers', methods=['GET'])
def get_numbers():
    return jsonify(numbers)

@app.route('/numbers', methods=['POST'])
def add_number():
    data = request.get_json()
    numbers.append(data['number'])
    return jsonify({"result": "Number added"}), 201

@app.route('/numbers/<int:index>', methods=['PUT'])
def update_number(index):
    data = request.get_json()
    if index >= len(numbers) or index < 0:
        return jsonify({"error": "Index out of range"}), 404
    numbers[index] = data['number']
    return jsonify({"result": "Number updated"})

@app.route('/numbers/<int:index>', methods=['DELETE'])
def delete_number(index):
    if index >= len(numbers) or index < 0:
        return jsonify({"error": "Index out of range"}), 404
    del numbers[index]
    return jsonify({"result": "Number deleted"})

if __name__ == '__main__':
    app.run(debug=True)
