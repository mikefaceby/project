from flask import Flask, request, jsonify
import requests
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

def forward_request(service_url, path):
    """Helper function to forward the request to the appropriate service."""
    try:
        url = f"{service_url}/{path}" if path else service_url
        logging.info(f"Forwarding {request.method} request to {url}")
        response = requests.request(
            method=request.method,
            url=url,
            json=request.get_json() if request.method in ['POST', 'PUT', 'PATCH'] else None
        )
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        logging.error(f"Error forwarding request: {str(e)}")
        return jsonify({"error": "Service request failed", "details": str(e)}), 500

# User & Employee Management Service
@app.route('/customers/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/customers', methods=['GET', 'POST'])
def customers_proxy(path=''):
    return forward_request('http://user_management_service:5000/customers', path)

@app.route('/employees/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/employees', methods=['GET', 'POST'])
def employees_proxy(path=''):
    return forward_request('http://user_management_service:5000/employees', path)

@app.route('/stores/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/stores', methods=['GET', 'POST'])
def stores_proxy(path=''):
    return forward_request('http://user_management_service:5000/stores', path)

# Product & Vendor Management Service
@app.route('/product_inventory/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/product_inventory', methods=['GET', 'POST'])
def product_inventory_proxy(path=''):
    return forward_request('http://product_management_service:5002/product_inventory', path)

@app.route('/vendorinfo/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/vendorinfo', methods=['GET', 'POST'])
def vendorinfo_proxy(path=''):
    return forward_request('http://product_management_service:5002/vendorinfo', path)

@app.route('/orders_ticket/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/orders_ticket', methods=['GET', 'POST'])
def orders_ticket_proxy(path=''):
    return forward_request('http://product_management_service:5002/orders_ticket', path)

@app.route('/orders/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/orders', methods=['GET', 'POST'])
def orders_proxy(path=''):
    return forward_request('http://product_management_service:5002/orders', path)

# Cart & Order Management Service
@app.route('/cart/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/cart', methods=['GET', 'POST'])
def cart_proxy(path=''):
    return forward_request('http://cart_order_management_service:5003/cart', path)

@app.route('/cart_inprogress/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/cart_inprogress', methods=['GET', 'POST'])
def cart_inprogress_proxy(path=''):
    return forward_request('http://cart_order_management_service:5003/cart_inprogress', path)

@app.route('/item_list/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/item_list', methods=['GET', 'POST'])
def item_list_proxy(path=''):
    return forward_request('http://cart_order_management_service:5003/item_list', path)

# Sales & Payment Service
@app.route('/ticket_system/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/ticket_system', methods=['GET', 'POST'])
def ticket_system_proxy(path=''):
    return forward_request('http://sales_payment_service:5001/ticket_system', path)

@app.route('/tax_table/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/tax_table', methods=['GET', 'POST'])
def tax_table_proxy(path=''):
    return forward_request('http://sales_payment_service:5001/tax_table', path)

@app.route('/registers_table/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/registers_table', methods=['GET', 'POST'])
def registers_table_proxy(path=''):
    return forward_request('http://sales_payment_service:5001/registers_table', path)

@app.route('/gift_card/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/gift_card', methods=['GET', 'POST'])
def gift_card_proxy(path=''):
    return forward_request('http://sales_payment_service:5001/gift_card', path)

# Return & Refund Service
@app.route('/return_table/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/return_table', methods=['GET', 'POST'])
def return_table_proxy(path=''):
    return forward_request('http://return_refund_service:5004/return_table', path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
