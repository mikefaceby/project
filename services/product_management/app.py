# services/user_service/app.py
from flask import Flask, request, jsonify
from mysql.connector import connect, Error
from config import Config

app = Flask(__name__)

# Verbindung zur Datenbank herstellen
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

# Produktverwaltung

# CREATE: Neuen Produkt hinzufügen
@app.route('/products', methods=['POST'])
def create_product():
    new_product = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO product_inventory (product_id, name, price, stock) VALUES (%s, %s, %s, %s)",
        (new_product['product_id'], new_product['name'], new_product['price'], new_product['stock'])
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(new_product), 201

# READ: Alle Produkte abrufen
@app.route('/products', methods=['GET'])
def get_products():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM product_inventory')
    products = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(products)

# READ: Einzelnes Produkt abrufen
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

# UPDATE: Produkt aktualisieren
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    updated_product = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE product_inventory SET name = %s, price = %s, stock = %s WHERE product_id = %s",
        (updated_product['name'], updated_product['price'], updated_product['stock'], product_id)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(updated_product)

# DELETE: Produkt löschen
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM product_inventory WHERE product_id = %s", (product_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Product deleted"})

# Lieferantenverwaltung

# CREATE: Neuen Lieferanten hinzufügen
@app.route('/vendors', methods=['POST'])
def create_vendor():
    new_vendor = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO vendorinfo (vendor_id, name, contact_info) VALUES (%s, %s, %s)",
        (new_vendor['vendor_id'], new_vendor['name'], new_vendor['contact_info'])
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(new_vendor), 201

# READ: Alle Lieferanten abrufen
@app.route('/vendors', methods=['GET'])
def get_vendors():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM vendorinfo')
    vendors = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(vendors)

# READ: Einzelnen Lieferanten abrufen
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

# UPDATE: Lieferanten aktualisieren
@app.route('/vendors/<int:vendor_id>', methods=['PUT'])
def update_vendor(vendor_id):
    updated_vendor = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE vendorinfo SET name = %s, contact_info = %s WHERE vendor_id = %s",
        (updated_vendor['name'], updated_vendor['contact_info'], vendor_id)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(updated_vendor)

# DELETE: Lieferanten löschen
@app.route('/vendors/<int:vendor_id>', methods=['DELETE'])
def delete_vendor(vendor_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM vendorinfo WHERE vendor_id = %s", (vendor_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Vendor deleted"})

# Bestellverwaltung

# CREATE: Neue Bestellung hinzufügen
@app.route('/orders', methods=['POST'])
def create_order():
    new_order = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO orders (order_id, product_id, quantity, vendor_id) VALUES (%s, %s, %s, %s)",
        (new_order['order_id'], new_order['product_id'], new_order['quantity'], new_order['vendor_id'])
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(new_order), 201

# READ: Alle Bestellungen abrufen
@app.route('/orders', methods=['GET'])
def get_orders():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM orders')
    orders = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(orders)

# READ: Einzelne Bestellung abrufen
@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM orders WHERE order_id = %s', (order_id,))
    order = cursor.fetchone()
    cursor.close()
    conn.close()

    if order:
        return jsonify(order)
    return jsonify({"error": "Order not found"}), 404

# UPDATE: Bestellung aktualisieren
@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    updated_order = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE orders SET product_id = %s, quantity = %s, vendor_id = %s WHERE order_id = %s",
        (updated_order['product_id'], updated_order['quantity'], updated_order['vendor_id'], order_id)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(updated_order)

# DELETE: Bestellung löschen
@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM orders WHERE order_id = %s", (order_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Order deleted"})

# Bestellticketverwaltung

# CREATE: Neues Bestellticket hinzufügen
@app.route('/orders/tickets', methods=['POST'])
def create_order_ticket():
    new_order_ticket = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO orders_ticket (ticket_id, order_id, status) VALUES (%s, %s, %s)",
        (new_order_ticket['ticket_id'], new_order_ticket['order_id'], new_order_ticket['status'])
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(new_order_ticket), 201

# READ: Alle Bestelltickets abrufen
@app.route('/orders/tickets', methods=['GET'])
def get_order_tickets():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM orders_ticket')
    order_tickets = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(order_tickets)

# READ: Einzelnes Bestellticket abrufen
@app.route('/orders/tickets/<int:ticket_id>', methods=['GET'])
def get_order_ticket(ticket_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM orders_ticket WHERE ticket_id = %s', (ticket_id,))
    order_ticket = cursor.fetchone()
    cursor.close()
    conn.close()

    if order_ticket:
        return jsonify(order_ticket)
    return jsonify({"error": "Order ticket not found"}), 404

# UPDATE: Bestellticket aktualisieren
@app.route('/orders/tickets/<int:ticket_id>', methods=['PUT'])
def update_order_ticket(ticket_id):
    updated_order_ticket = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE orders_ticket SET order_id = %s, status = %s WHERE ticket_id = %s",
        (updated_order_ticket['order_id'], updated_order_ticket['status'], ticket_id)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(updated_order_ticket)

# DELETE: Bestellticket löschen
@app.route('/orders/tickets/<int:ticket_id>', methods=['DELETE'])
def delete_order_ticket(ticket_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM orders_ticket WHERE ticket_id = %s", (ticket_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Order ticket deleted"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)  # Port 5002 für den Produkt-Microservice
