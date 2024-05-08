from flask import Flask, request, jsonify
app= Flask(__name__)

virtual_servers = []
used_storage = 0
total_storage = 1000

@app.route('/create_server' , methods=['POST'])
def create_server():
    global used_storage
    data = request.json

    server_name , cpu , ram = data.get('server_name') , int(data.get('cpu')) , int(data.get('ram'))

    virtual_server = {"name" :server_name , "cpu":cpu , "ram":ram}
    virtual_servers.append(virtual_server)

    used_storage += cpu * ram

    return jsonify({"message" :"Server created succesfuly" ,
                    "server" : virtual_server})

@app.route('/list_servers' , methods=['GET'])
def list_server():
    return jsonify({"servers" : virtual_servers})

@app.route('/get_storage_statur' , methods=['GET'])
def get_server():
    return jsonify({"used" : used_storage , "total" : total_storage})

app.run()