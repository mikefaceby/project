from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Benutzer- und Mitarbeiterverwaltung (User & Employee Management Service)
@app.route('/customers/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/customers', methods=['GET', 'POST'])
def customers_proxy(path=''):
    url = f'http://user_management_service:5000/customers/{path}'
    response = requests.request(method=request.method, url=url, json=request.get_json())
    return jsonify(response.json()), response.status_code

@app.route('/employees/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/employees', methods=['GET', 'POST'])
def employees_proxy(path=''):
    url = f'http://user_management_service:5000/employees/{path}'
    response = requests.request(method=request.method, url=url, json=request.get_json())
    return jsonify(response.json()), response.status_code

@app.route('/stores/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/stores', methods=['GET', 'POST'])
def stores_proxy(path=''):
    url = f'http://user_management_service:5000/stores/{path}'
    response = requests.request(method=request.method, url=url, json=request.get_json())
    return jsonify(response.json()), response.status_code

# Produkt- und Lieferantenverwaltung (Product & Vendor Management Service)
@app.route('/product_inventory/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/product_inventory', methods=['GET', 'POST'])
def product_inventory_proxy(path=''):
    url = f'http://product_management_service:5002/product_inventory/{path}'
    response = requests.request(method=request.method, url=url, json=request.get_json())
    return jsonify(response.json()), response.status_code

@app.route('/vendorinfo/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/vendorinfo', methods=['GET', 'POST'])
def vendorinfo_proxy(path=''):
    url = f'http://product_management_service:5002/vendorinfo/{path}'
    response = requests.request(method=request.method, url=url, json=request.get_json())
    return jsonify(response.json()), response.status_code

@app.route('/orders_ticket/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/orders_ticket', methods=['GET', 'POST'])
def orders_ticket_proxy(path=''):
    url = f'http://product_management_service:5002/orders_ticket/{path}'
    response = requests.request(method=request.method, url=url, json=request.get_json())
    return jsonify(response.json()), response.status_code

@app.route('/orders/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/orders', methods=['GET', 'POST'])
def orders_proxy(path=''):
    url = f'http://product_management_service:5002/orders/{path}'
    response = requests.request(method=request.method, url=url, json=request.get_json())
    return jsonify(response.json()), response.status_code

# Einkaufswagen- und Bestellmanagement (Cart & Order Management Service)
@app.route('/cart/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/cart', methods=['GET', 'POST'])
def cart_proxy(path=''):
    url = f'http://cart_order_management_service:5003/cart/{path}'
    response = requests.request(method=request.method, url=url, json=request.get_json())
    return jsonify(response.json()), response.status_code

@app.route('/cart_inprogress/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/cart_inprogress', methods=['GET', 'POST'])
def cart_inprogress_proxy(path=''):
    url = f'http://cart_order_management_service:5003/cart_inprogress/{path}'
    response = requests.request(method=request.method, url=url, json=request.get_json())
    return jsonify(response.json()), response.status_code

@app.route('/item_list/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/item_list', methods=['GET', 'POST'])
def item_list_proxy(path=''):
    url = f'http://cart_order_management_service:5003/item_list/{path}'
    response = requests.request(method=request.method, url=url, json=request.get_json())
    return jsonify(response.json()), response.status_code

# Verkaufs- und Zahlungssystem (Sales & Payment Service)
@app.route('/ticket_system/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/ticket_system', methods=['GET', 'POST'])
def ticket_system_proxy(path=''):
    url = f'http://sales_payment_service:5001/ticket_system/{path}'
    response = requests.request(method=request.method, url=url, json=request.get_json())
    return jsonify(response.json()), response.status_code

@app.route('/tax_table/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/tax_table', methods=['GET', 'POST'])
def tax_table_proxy(path=''):
    url = f'http://sales_payment_service:5001/tax_table/{path}'
    response = requests.request(method=request.method, url=url, json=request.get_json())
    return jsonify(response.json()), response.status_code

@app.route('/registers_table/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/registers_table', methods=['GET', 'POST'])
def registers_table_proxy(path=''):
    url = f'http://sales_payment_service:5001/registers_table/{path}'
    response = requests.request(method=request.method, url=url, json=request.get_json())
    return jsonify(response.json()), response.status_code

@app.route('/gift_card/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/gift_card', methods=['GET', 'POST'])
def gift_card_proxy(path=''):
    url = f'http://sales_payment_service:5001/gift_card/{path}'
    response = requests.request(method=request.method, url=url, json=request.get_json())
    return jsonify(response.json()), response.status_code

# Rückgabe- und Umtauschverwaltung (Return & Refund Service)
@app.route('/return_table/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/return_table', methods=['GET', 'POST'])
def return_table_proxy(path=''):
    url = f'http://return_refund_service:5004/return_table/{path}'
    response = requests.request(method=request.method, url=url, json=request.get_json())
    return jsonify(response.json()), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)