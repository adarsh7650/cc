#book 
from flask import Flask,jsonify,request

app = Flask(__name__)

book = [{"id":1,"author":"author1","title":"black clover"},{"id":2,"author":"author2","title":"jjk"}]

@app.route("/view/books",methods=["GET"])
def view_books():
    return jsonify(book),200

@app.route("/view/book/<int:id>",methods=["GET"])
def view_book(id):
    for i in book:
        if(i['id']==id):
            return jsonify(i),200
    return jsonify({"error":"book not found"}),400

@app.route("/add/book",methods=["POST"])
def add_book():
    if(request.is_json):
        json_data = request.get_json()
    else:
        return jsonify({"msg":"only json type data is accepted"}),200
    
    required_content = ["id","author","title"]
    list_of_keys = list(json_data.keys())
    
    for content in required_content:
        if(content not in list_of_keys):
            return jsonify({"msg":f"{content} is required field"}),400
    
    if(len(required_content) != len(list_of_keys)):
        return jsonify({"msg":"extra parameters are not allowed"}),400

    book.append(json_data)
    return jsonify(book),201

@app.route("/delete/book/<int:id>",methods=["DELETE"])
def delete_book(id):
    for i in range(len(book)):
        if(book[i]["id"]==id):
            book.pop(i)
            return jsonify(book),200
    
    return jsonify({"msg":"no such book exists"}),400


app.run()