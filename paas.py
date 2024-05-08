from flask import Flask , request , jsonify

app= Flask(__name__)
application = []

@app.route('/create_application' , methods=['POST'])
def create_application():
    data = request.json

    app_name = data.get('app_name')
    app_type = data.get('app_type')

    new_app = {"app_name" : app_name , "app_type" : app_type}

    application.append(new_app)
    return jsonify({"msg" :"done " , "application" : new_app})

@app.route('/list_application' , methods=['GET'])
def list_application():
    return jsonify({"application " : application})

app.run()