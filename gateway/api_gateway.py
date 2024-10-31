# gateway/api-gateway.py
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Route für User-Service
@app.route('/users/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def users_proxy(path):
    url = f'http://user_management_service:5000/{path}'  # URL des User-Service Containers
    response = requests.request(method=request.method, url=url, json=request.get_json())
    
        # Protokolliere den Statuscode und die Antwort
    print(f'Status Code: {response.status_code}')
    print(f'Response Text: {response.text}')
    
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

# Route für Payment-Service
@app.route('/payments/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def payments_proxy(path):
    url = f'http://sales_payment_service:5001/{path}'  # URL des Payment-Service Containers
    response = requests.request(method=request.method, url=url, json=request.get_json())
    return jsonify(response.json()), response.status_code

# Route für Refund-Service
@app.route('/refunds/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def refunds_proxy(path):
    url = f'http://return_refund_service:5004/{path}'  # URL des Refund-Service Containers
    response = requests.request(method=request.method, url=url, json=request.get_json())
    return jsonify(response.json()), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)  # Gateway läuft auf Port 8000
