from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Route für User-Service
@app.route('/users/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def users_proxy(path):
    url = f'http://user_management_service:5000/{path}'  # URL des User-Service Containers
    response = requests.request(method=request.method, url=url, json=request.get_json())
    return jsonify(response.json()), response.status_code

# Route für Product-Service
@app.route('/products/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def products_proxy(path):
    url = f'http://product_management_service:5002/{path}'  # URL des Product-Service Containers
    response = requests.request(method=request.method, url=url, json=request.get_json())
    return jsonify(response.json()), response.status_code

# Route für Cart-Service
@app.route('/carts/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def carts_proxy(path):
    url = f'http://cart_order_management_service:5003/{path}'  # URL des Cart-Service Containers
    response = requests.request(method=request.method, url=url, json=request.get_json())
    return jsonify(response.json()), response.status_code

# Route für Sales-Service
@app.route('/sales/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def sales_proxy(path):
    url = f'http://sales_payment_service:5001/{path}'  # URL des Sales-Service Containers
    response = requests.request(method=request.method, url=url, json=request.get_json())
    return jsonify(response.json()), response.status_code

# Route für Return-Service
@app.route('/returns/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def returns_proxy(path):
    url = f'http://return_refund_service:5004/{path}'  # URL des Return-Service Containers
    response = requests.request(method=request.method, url=url, json=request.get_json())
    return jsonify(response.json()), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)