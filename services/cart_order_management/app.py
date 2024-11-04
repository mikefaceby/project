# services/cart_order_management/app.py
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

# Cart Management

# CREATE: Add a new cart
@app.route('/cart', methods=['POST'])
def create_cart():
    new_cart = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO cart (CID, qty, product_id) VALUES (%s, %s, %s)",
        (new_cart['CID'], new_cart['qty'], new_cart['product_id'])
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(new_cart), 201

# READ: Retrieve all carts
@app.route('/cart', methods=['GET'])
def get_carts():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM cart')
    carts = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(carts)

# READ: Retrieve a single cart
@app.route('/cart/<int:cart_id>', methods=['GET'])
def get_cart(cart_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM cart WHERE cart_id = %s', (cart_id,))
    cart = cursor.fetchone()
    cursor.close()
    conn.close()

    if cart:
        return jsonify(cart)
    return jsonify({"error": "Cart not found"}), 404

# UPDATE: Update a cart
@app.route('/cart/<int:cart_id>', methods=['PUT'])
def update_cart(cart_id):
    updated_cart = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE cart SET CID = %s, qty = %s, product_id = %s WHERE cart_id = %s",
        (updated_cart['CID'], updated_cart['qty'], updated_cart['product_id'], cart_id)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(updated_cart)

# DELETE: Delete a cart
@app.route('/cart/<int:cart_id>', methods=['DELETE'])
def delete_cart(cart_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM cart WHERE cart_id = %s", (cart_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Cart deleted"})

# Cart In Progress Management

# CREATE: Add a new cart in progress
@app.route('/cart_inprogress', methods=['POST'])
def create_cart_in_progress():
    new_cart_in_progress = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO cart_inprogress (customer_id, ticket_id) VALUES (%s, %s)",
        (new_cart_in_progress['customer_id'], new_cart_in_progress['ticket_id'])
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(new_cart_in_progress), 201

# READ: Retrieve all carts in progress
@app.route('/cart_inprogress', methods=['GET'])
def get_carts_in_progress():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM cart_inprogress')
    carts_in_progress = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(carts_in_progress)

# READ: Retrieve a single cart in progress
@app.route('/cart_inprogress/<int:CID>', methods=['GET'])
def get_cart_in_progress(CID):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM cart_inprogress WHERE CID = %s', (CID,))
    cart_in_progress = cursor.fetchone()
    cursor.close()
    conn.close()

    if cart_in_progress:
        return jsonify(cart_in_progress)
    return jsonify({"error": "Cart in progress not found"}), 404

# UPDATE: Update a cart in progress
@app.route('/cart_inprogress/<int:CID>', methods=['PUT'])
def update_cart_in_progress(CID):
    updated_cart_in_progress = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE cart_inprogress SET customer_id = %s, ticket_id = %s WHERE CID = %s",
        (updated_cart_in_progress['customer_id'], updated_cart_in_progress['ticket_id'], CID)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(updated_cart_in_progress)

# DELETE: Delete a cart in progress
@app.route('/cart_inprogress/<int:CID>', methods=['DELETE'])
def delete_cart_in_progress(CID):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM cart_inprogress WHERE CID = %s", (CID,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Cart in progress deleted"})

# Item List Management

# CREATE: Add a new item
@app.route('/item_list', methods=['POST'])
def create_item():
    new_item = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO item_list (CID, qty, product_id) VALUES (%s, %s, %s)",
        (new_item['CID'], new_item['qty'], new_item['product_id'])
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(new_item), 201

# READ: Retrieve all items
@app.route('/item_list', methods=['GET'])
def get_items():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM item_list')
    items = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(items)

# READ: Retrieve a single item
@app.route('/item_list/<int:TID>', methods=['GET'])
def get_item(TID):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM item_list WHERE TID = %s', (TID,))
    item = cursor.fetchone()
    cursor.close()
    conn.close()

    if item:
        return jsonify(item)
    return jsonify({"error": "Item not found"}), 404

# UPDATE: Update an item
@app.route('/item_list/<int:TID>', methods=['PUT'])
def update_item(TID):
    updated_item = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE item_list SET CID = %s, qty = %s, product_id = %s WHERE TID = %s",
        (updated_item['CID'], updated_item['qty'], updated_item['product_id'], TID)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(updated_item)

# DELETE: Delete an item
@app.route('/item_list/<int:TID>', methods=['DELETE'])
def delete_item(TID):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM item_list WHERE TID = %s", (TID,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Item deleted"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)  # Cart Order Management service running on port 5003
