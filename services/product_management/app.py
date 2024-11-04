# services/product_management/app.py
from flask import Flask, request, jsonify
from mysql.connector import connect, Error
from config import Config

app = Flask(__name__)

# Establish database connection
def get_db_connection():
    try:
        connection = connect(
            host=Config.DB_HOST,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            database=Config.DB_NAME,
            port=Config.DB_PORT
        )
        return connection
    except Error as e:
        print(f"Error connecting to database: {e}")
        return None

@app.route('/')
def index():
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE();")
        db_name = cursor.fetchone()[0]
        cursor.close()
        connection.close()
        return f"Connected to database: {db_name}"
    return "Database connection failed"

# Product Management

# CREATE: Add a new product
@app.route('/products', methods=['POST'])
def create_product():
    new_product = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO product_inventory (brand, description, productName, productType, productSubType, unit_price, cost, in_stock, vendor_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (
            new_product['brand'],
            new_product['description'],
            new_product['productName'],
            new_product['productType'],
            new_product['productSubType'],
            new_product['unit_price'],
            new_product['cost'],
            new_product['in_stock'],
            new_product['vendor_id']
        )
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(new_product), 201

# READ: Retrieve all products
@app.route('/products', methods=['GET'])
def get_products():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM product_inventory')
    products = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(products)

# READ: Retrieve a single product
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM product_inventory WHERE product_id = %s', (product_id,))
    product = cursor.fetchone()
    cursor.close()
    conn.close()

    if product:
        return jsonify(product)
    return jsonify({"error": "Product not found"}), 404

# UPDATE: Update a product
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    updated_product = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE product_inventory 
        SET brand = %s, description = %s, productName = %s, productType = %s, productSubType = %s,
            unit_price = %s, cost = %s, in_stock = %s, vendor_id = %s
        WHERE product_id = %s
        """,
        (
            updated_product['brand'],
            updated_product['description'],
            updated_product['productName'],
            updated_product['productType'],
            updated_product['productSubType'],
            updated_product['unit_price'],
            updated_product['cost'],
            updated_product['in_stock'],
            updated_product['vendor_id'],
            product_id
        )
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(updated_product)

# DELETE: Delete a product
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM product_inventory WHERE product_id = %s", (product_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Product deleted"})

# Vendor Management

# CREATE: Add a new vendor
@app.route('/vendors', methods=['POST'])
def create_vendor():
    new_vendor = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO vendorinfo (company_name, department, street_address, city, state, zip_code, phone_number, fax_number, email)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (
            new_vendor['company_name'],
            new_vendor['department'],
            new_vendor['street_address'],
            new_vendor['city'],
            new_vendor['state'],
            new_vendor['zip_code'],
            new_vendor['phone_number'],
            new_vendor['fax_number'],
            new_vendor['email']
        )
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(new_vendor), 201

# READ: Retrieve all vendors
@app.route('/vendors', methods=['GET'])
def get_vendors():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM vendorinfo')
    vendors = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(vendors)

# READ: Retrieve a single vendor
@app.route('/vendors/<int:vendor_id>', methods=['GET'])
def get_vendor(vendor_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM vendorinfo WHERE vendor_id = %s', (vendor_id,))
    vendor = cursor.fetchone()
    cursor.close()
    conn.close()

    if vendor:
        return jsonify(vendor)
    return jsonify({"error": "Vendor not found"}), 404

# UPDATE: Update a vendor
@app.route('/vendors/<int:vendor_id>', methods=['PUT'])
def update_vendor(vendor_id):
    updated_vendor = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE vendorinfo 
        SET company_name = %s, department = %s, street_address = %s, city = %s, 
            state = %s, zip_code = %s, phone_number = %s, fax_number = %s, email = %s
        WHERE vendor_id = %s
        """,
        (
            updated_vendor['company_name'],
            updated_vendor['department'],
            updated_vendor['street_address'],
            updated_vendor['city'],
            updated_vendor['state'],
            updated_vendor['zip_code'],
            updated_vendor['phone_number'],
            updated_vendor['fax_number'],
            updated_vendor['email'],
            vendor_id
        )
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(updated_vendor)

# DELETE: Delete a vendor
@app.route('/vendors/<int:vendor_id>', methods=['DELETE'])
def delete_vendor(vendor_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM vendorinfo WHERE vendor_id = %s", (vendor_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Vendor deleted"})

# Order Management

# CREATE: Add a new order
@app.route('/orders', methods=['POST'])
def create_order():
    new_order = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO orders (OTID, stock_amount, product_id)
        VALUES (%s, %s, %s)
        """,
        (
            new_order['OTID'],
            new_order['stock_amount'],
            new_order['product_id']
        )
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(new_order), 201

# READ: Retrieve all orders
@app.route('/orders', methods=['GET'])
def get_orders():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM orders')
    orders = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(orders)

# READ: Retrieve a single order
@app.route('/orders/<int:OID>', methods=['GET'])
def get_order(OID):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM orders WHERE OID = %s', (OID,))
    order = cursor.fetchone()
    cursor.close()
    conn.close()

    if order:
        return jsonify(order)
    return jsonify({"error": "Order not found"}), 404

# UPDATE: Update an order
@app.route('/orders/<int:OID>', methods=['PUT'])
def update_order(OID):
    updated_order = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE orders 
        SET OTID = %s, stock_amount = %s, product_id = %s 
        WHERE OID = %s
        """,
        (
            updated_order['OTID'],
            updated_order['stock_amount'],
            updated_order['product_id'],
            OID
        )
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(updated_order)

# DELETE: Delete an order
@app.route('/orders/<int:OID>', methods=['DELETE'])
def delete_order(OID):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM orders WHERE OID = %s", (OID,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Order deleted"})

# Order Ticket Management

# CREATE: Add a new order ticket
@app.route('/orders/tickets', methods=['POST'])
def create_order_ticket():
    new_order_ticket = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO orders_ticket (
            date, time, quantity, subtotal, total, discount, tax, tax_rate, cash, 
            credit, status, employee_id, vendor_id
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (
            new_order_ticket['date'],
            new_order_ticket['time'],
            new_order_ticket['quantity'],
            new_order_ticket['subtotal'],
            new_order_ticket['total'],
            new_order_ticket['discount'],
            new_order_ticket['tax'],
            new_order_ticket['tax_rate'],
            new_order_ticket['cash'],
            new_order_ticket['credit'],
            new_order_ticket['status'],
            new_order_ticket['employee_id'],
            new_order_ticket['vendor_id']
        )
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(new_order_ticket), 201

# READ: Retrieve all order tickets
@app.route('/orders/tickets', methods=['GET'])
def get_order_tickets():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM orders_ticket')
    order_tickets = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(order_tickets)

# READ: Retrieve a single order ticket
@app.route('/orders/tickets/<int:OTID>', methods=['GET'])
def get_order_ticket(OTID):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM orders_ticket WHERE OTID = %s', (OTID,))
    order_ticket = cursor.fetchone()
    cursor.close()
    conn.close()

    if order_ticket:
        return jsonify(order_ticket)
    return jsonify({"error": "Order ticket not found"}), 404

# UPDATE: Update an order ticket
@app.route('/orders/tickets/<int:OTID>', methods=['PUT'])
def update_order_ticket(OTID):
    updated_order_ticket = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE orders_ticket 
        SET date = %s, time = %s, quantity = %s, subtotal = %s, total = %s, 
            discount = %s, tax = %s, tax_rate = %s, cash = %s, credit = %s, 
            status = %s, employee_id = %s, vendor_id = %s
        WHERE OTID = %s
        """,
        (
            updated_order_ticket['date'],
            updated_order_ticket['time'],
            updated_order_ticket['quantity'],
            updated_order_ticket['subtotal'],
            updated_order_ticket['total'],
            updated_order_ticket['discount'],
            updated_order_ticket['tax'],
            updated_order_ticket['tax_rate'],
            updated_order_ticket['cash'],
            updated_order_ticket['credit'],
            updated_order_ticket['status'],
            updated_order_ticket['employee_id'],
            updated_order_ticket['vendor_id'],
            OTID
        )
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(updated_order_ticket)

# DELETE: Delete an order ticket
@app.route('/orders/tickets/<int:OTID>', methods=['DELETE'])
def delete_order_ticket(OTID):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM orders_ticket WHERE OTID = %s", (OTID,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Order ticket deleted"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)  # Product service running on port 5002
