from flask import Flask, jsonify, request
from structure import card,cart,order,store,user,comment
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/get/<path>/', methods=['GET'])
def GetMethod(path):
    result = None
    if path == "searchCard":
        result = card.searchCard(request.get_json())
    elif path == "actualCard":
        result = card.GetActualCard(request.get_json())
    elif path == "shoppingCart":
        result = cart.GetCart(request.get_json())
    elif path == "store":
        result = store.GetStore(request.get_json())
    elif path == "order":
        result = order.GetOrder(request.get_json())
    
    return jsonify(result)

@app.route('/login', methods=['GET'])
def login():
    return jsonify(user.loginUser(request.get_json()))

@app.route('/register', methods=['POST'])
def register():
    result = user.registerUser(request.get_json())
    return jsonify(result)

@app.route('/add/<path>/', methods=['POST'])
def AddMethod(path):
    result = None
    if path == "comment":
        result = comment.AddComment(request.get_json())
    elif path == "storeCard":
        result = card.AddCard(request.get_json())
    elif path == "actualCard":
        result = card.AddActualCard(request.get_json())
    elif path == "shoppingCart":
        result = card.AddCardToCart(request.get_json())
    elif path == "order":
        result = card.Addorder(request.get_json())
    return jsonify(result)

@app.route('/update/<path>/', methods=['PUT'])
def Update(path):
    result = None
    if path == "storeCard":
        result = card.updateCard(request.get_json())
    elif path == "actualCard":
        result = card.updateActualCard(request.get_json())
    return jsonify(result)

@app.route('/remove/<path>/', methods=['DELETE'])
def Remove(path):
    result = None
    if path == "storeCard":
        result = card.removeCard(request.get_json())
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug = True)