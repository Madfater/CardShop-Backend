from flask import Flask, jsonify, request
from structure import card,cart,order,store,user,comment
from flask_cors import CORS

class PrefixMiddleware(object):

    def __init__(self, app, prefix=''):
        self.app = app
        self.prefix = prefix

    def __call__(self, environ, start_response):

        if environ['PATH_INFO'].startswith(self.prefix):
            environ['PATH_INFO'] = environ['PATH_INFO'][len(self.prefix):]
            environ['SCRIPT_NAME'] = self.prefix
            return self.app(environ, start_response)
        else:
            start_response('404', [('Content-Type', 'text/plain')])
            return ["This url does not belong to the app.".encode()]

app = Flask(__name__)
CORS(app)
app.wsgi_app = PrefixMiddleware(app.wsgi_app, prefix='/api')

# User
@app.route('/user/<path:method>', methods = ['POST'])
def UserApproach(method):
    if method == "login":
        return jsonify(user.Login(request.get_json()))
    elif method == "register":
        return jsonify(user.Register(request.get_json()))
    
@app.route('/user/name', methods = ['GET'])
def GetUserName():
    id = request.args.get('id')
    return jsonify(user.GetName(id))

# ShoppingCart
@app.route('/cart', methods = ['GET'])
def Cart():
    userId = request.args.get('userId')
    page = request.args.get('page', default = 1, type = int)
    pageLimit = request.args.get('page_limit', default = 30, type = int)
    return jsonify(cart.lookCart(userId,page,pageLimit))

@app.route('/cart', methods = ['POST'])
def AddCardToCart():
    return jsonify(cart.addCard(request.get_json()))

@app.route('/cart', methods = ['DELETE'])
def RemoveCardFromCart():
    userId = request.args.get('userId')
    cardId = request.args.get('cardId')
    return jsonify(cart.removeCard(userId,cardId))

@app.route('/cart', methods = ['PUT'])
def UpdateCardFromCart():
    return jsonify(cart.updateCard(request.get_json()))

# Store
@app.route('/store', methods = ['GET'])
def Store():
    storeId = request.args.get('id')
    return jsonify(store.GetStore(storeId))

@app.route('/store/search', methods = ['GET'])
def SearchStore():
    param = request.args.get('keyword')
    page = request.args.get('page', default = 1, type = int)
    pageLimit = request.args.get('pageLimit', default = 30, type = int)
    return jsonify(store.SearchStore(param,page,pageLimit))

@app.route('/store', methods = ['PUT'])
def UpdateStore():
    return jsonify(store.updateStore(request.get_json()))

# Actual Card
@app.route('/actualCard', methods = ['GET'])
def ActualCard():
    cardId = request.args.get('id')
    return jsonify(card.GetActualCard(cardId))

@app.route('/actualCard', methods = ['POST'])
def AddActualCard():
    return jsonify(card.AddActualCard(request.get_json()))

@app.route('/actualCard', methods = ['PUT'])
def UpdateActualCard():
    return jsonify(card.updateActualCard(request.get_json()))

@app.route('/actualCard', methods = ['DELETE'])
def RemoveActualCard():
    return jsonify(card.removeActualCard(request.get_json()))

# comment
@app.route('/comment', methods = ['GET'])
def Comment():
    storeId = request.args.get('storeId')
    page = request.args.get('page', default = 1 , type = int)
    pageLimit = request.args.get('pageLimit', default = 30 , type = int)
    return jsonify(comment.lookComment(storeId,page,pageLimit))

@app.route('/comment', methods = ['POST'])
def AddComment():
    return jsonify(comment.AddComment(request.get_json()))

@app.route('/comment', methods = ['PUT'])
def UpdateComment():
    return jsonify(comment.updateComment(request.get_json()))

@app.route('/comment', methods = ['DELETE'])
def RemoveComment():
    return jsonify(comment.removeComment(request.get_json()))

# order
@app.route('/order', methods = ['GET'])
def Order():
    id = request.args.get('id')
    page = request.args.get('page', default = 1 , type = int)
    pageLimit = request.args.get('pageLimit', default = 30 , type = int)
    return jsonify(order.lookOrder(id, page, pageLimit))

@app.route('/order', methods = ['POST'])
def AddOrder():
    return jsonify(order.addOrder(request.get_json()))

@app.route('/order', methods = ['PUT'])
def UpdateOrder():
    return jsonify(order.updateOrder(request.get_json()))

@app.route('/order', methods = ['DELETE'])
def RemoveOrder():
    return jsonify(order.removeOrder(request.get_json()))

# Store Card
@app.route('/card', methods = ['GET'])
def Card():
    id = request.args.get('id')
    return jsonify(card.GetStoreCard(id))

@app.route('/card/search', methods = ['GET'])
def SearchCard():
    param = request.args.get('keyword')
    catagory = request.args.get('catagory')
    page = request.args.get('page', default = 1, type = int)
    pageLimit = request.args.get('pageLimit', default = 30, type = int)
    orderWay = request.args.get('orderWay', default = "id", type = str)
    ascending = request.args.get('ascending', default = True, type = lambda x: x.lower() == 'true')
    return jsonify(card.searchStoreCard(param, catagory, page, pageLimit, orderWay, ascending))

@app.route('/card/store', methods = ['GET'])
def StoreCard():
    storeId = request.args.get('storeId')
    page = request.args.get('page', default = 1, type = int)
    pageLimit = request.args.get('pageLimit', default = 30, type = int)
    orderWay = request.args.get('orderWay', default = "id", type = str)
    ascending = request.args.get('ascending', default = True, type = lambda x: x.lower() == 'true')
    return jsonify(card.lookCardInStore(storeId, page, pageLimit, orderWay, ascending))

@app.route('/card', methods = ['POST'])
def AddCard():
    return jsonify(card.AddStoreCard(request.get_json()))

@app.route('/card', methods = ['PUT'])
def UpdateCard():
    return jsonify(card.updateStoreCard(request.get_json()))

@app.route('/card', methods = ['DELETE'])
def RemoveCard():
    userId = request.args.get('userId')
    cardId = request.args.get('cardId')
    return jsonify(card.removeStoreCard(userId,cardId))

if __name__ == '__main__':
    app.run(debug = True, host="0.0.0.0")