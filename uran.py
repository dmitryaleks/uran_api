#!flask/bin/python
from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request

app = Flask(__name__)

# fixtures for the static data so that we serve at least some data from the start
orders = [
    {
        'id': 1,
        'instrument': '6758.T',
        'quantity': 10000,
        'price': 3800
    },
    {
        'id': 2,
        'instrument': '6753.T',
        'quantity': 5000,
        'price': 2700
    },
    {
        'id': 3,
        'instrument': '6751.T',
        'quantity': 8000,
        'price': 3200
    }
]

@app.route('/uran/api/v1.0/orders', methods=['GET'])
def get_orders():
    return jsonify({'orders': orders})

@app.route('/uran/api/v1.0/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = [order for order in orders if order['id'] == order_id]
    if len(order) == 0:
        abort(404)
    return jsonify({'order': order[0]})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/uran/api/v1.0/orders', methods=['POST'])
def create_order():
    if not request.json or not 'instrument' in request.json:
        abort(400)
    order = {
        'id': orders[-1]['id'] + 1,
        'instrument': request.json['instrument'],
        'quantity': request.json['quantity'],
        'price': request.json['price']
    }
    orders.append(order)
    return jsonify({'order': order}), 201

@app.route('/uran/api/v1.0/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    order = [order for order in orders if order['id'] == order_id]
    if len(order) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    order[0]['title'] = request.json.get('title', order[0]['title'])
    order[0]['description'] = request.json.get('description', order[0]['description'])
    order[0]['done'] = request.json.get('done', order[0]['done'])
    return jsonify({'order': order[0]})

@app.route('/uran/api/v1.0/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    order = [order for order in orders if order['id'] == order_id]
    if len(order) == 0:
        abort(404)
    orders.remove(order[0])
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)
