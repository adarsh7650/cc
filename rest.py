#single variable 
from flask import Flask , request , jsonify

app = Flask(__name__)
number = []

@app.route('/numbers' , methods=['GET'])
def get_numbers():
    return jsonify(number)

@app.route('/numbers' , methods=['POST'])
def add_number():
    data = request.get_json()
    number.append(data['number'])
    return jsonify({"result" :"Number added"})

@app.route('/numbers/<int:index>' , methods=['PUT'])
def update_number(index):
    data = request.get_json()
    number[index] = data['number']
    return jsonify({"result" :"Number updated"})

@app.route('/numbers/<int:index>', methods=['DELETE'])
def delete_number(index):
    del number[index]
    return jsonify({"result" :"number deleted"})

if __name__ == '__main__':
    app.run(debug=True)