# services/cart_service/app.py
from flask import Flask, request, jsonify
import os
import mysql.connector

app = Flask(__name__)

# Verbindung zur Datenbank herstellen
def get_db_connection():
    connection = mysql.connector.connect(
        host='[SERVICE_DB_HOST]',  # Hostname des MariaDB-Containers
        user=os.getenv('[SERVICE_DB_USER]'),
        password=os.getenv('[SERVICE_DB_PASSWORD]'),
        database=os.getenv('[SERVICE_DB_NAME]')
    )
    return connection

# Einkaufswagenverwaltung

# CREATE: Neuen Einkaufswagen hinzufügen
@app.route('/carts', methods=['POST'])
def create_cart():
    new_cart = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO cart (cart_id, customer_id, total_price) VALUES (%s, %s, %s)",
        (new_cart['cart_id'], new_cart['customer_id'], new_cart['total_price'])
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(new_cart), 201

# READ: Alle Einkaufswagen abrufen
@app.route('/carts', methods=['GET'])
def get_carts():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM cart')
    carts = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(carts)

# READ: Einzelnen Einkaufswagen abrufen
@app.route('/carts/<int:cart_id>', methods=['GET'])
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

# UPDATE: Einkaufswagen aktualisieren
@app.route('/carts/<int:cart_id>', methods=['PUT'])
def update_cart(cart_id):
    updated_cart = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE cart SET customer_id = %s, total_price = %s WHERE cart_id = %s",
        (updated_cart['customer_id'], updated_cart['total_price'], cart_id)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(updated_cart)

# DELETE: Einkaufswagen löschen
@app.route('/carts/<int:cart_id>', methods=['DELETE'])
def delete_cart(cart_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM cart WHERE cart_id = %s", (cart_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Cart deleted"})

# Einkaufswagen in Bearbeitung

# CREATE: Neuen Einkaufswagen in Bearbeitung hinzufügen
@app.route('/carts/inprogress', methods=['POST'])
def create_cart_in_progress():
    new_cart_in_progress = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO cart_inprogress (cart_id, customer_id) VALUES (%s, %s)",
        (new_cart_in_progress['cart_id'], new_cart_in_progress['customer_id'])
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(new_cart_in_progress), 201

# READ: Alle Einkaufswagen in Bearbeitung abrufen
@app.route('/carts/inprogress', methods=['GET'])
def get_carts_in_progress():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM cart_inprogress')
    carts_in_progress = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(carts_in_progress)

# READ: Einzelnen Einkaufswagen in Bearbeitung abrufen
@app.route('/carts/inprogress/<int:cart_id>', methods=['GET'])
def get_cart_in_progress(cart_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM cart_inprogress WHERE cart_id = %s', (cart_id,))
    cart_in_progress = cursor.fetchone()
    cursor.close()
    conn.close()

    if cart_in_progress:
        return jsonify(cart_in_progress)
    return jsonify({"error": "Cart in progress not found"}), 404

# UPDATE: Einkaufswagen in Bearbeitung aktualisieren
@app.route('/carts/inprogress/<int:cart_id>', methods=['PUT'])
def update_cart_in_progress(cart_id):
    updated_cart_in_progress = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE cart_inprogress SET customer_id = %s WHERE cart_id = %s",
        (updated_cart_in_progress['customer_id'], cart_id)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(updated_cart_in_progress)

# DELETE: Einkaufswagen in Bearbeitung löschen
@app.route('/carts/inprogress/<int:cart_id>', methods=['DELETE'])
def delete_cart_in_progress(cart_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM cart_inprogress WHERE cart_id = %s", (cart_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Cart in progress deleted"})

# Artikelverwaltung

# CREATE: Neuen Artikel hinzufügen
@app.route('/items', methods=['POST'])
def create_item():
    new_item = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO item_list (item_id, cart_id, product_id, quantity) VALUES (%s, %s, %s, %s)",
        (new_item['item_id'], new_item['cart_id'], new_item['product_id'], new_item['quantity'])
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(new_item), 201

# READ: Alle Artikel abrufen
@app.route('/items', methods=['GET'])
def get_items():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM item_list')
    items = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(items)

# READ: Einzelnen Artikel abrufen
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM item_list WHERE item_id = %s', (item_id,))
    item = cursor.fetchone()
    cursor.close()
    conn.close()

    if item:
        return jsonify(item)
    return jsonify({"error": "Item not found"}), 404

# UPDATE: Artikel aktualisieren
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    updated_item = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE item_list SET cart_id = %s, product_id = %s, quantity = %s WHERE item_id = %s",
        (updated_item['cart_id'], updated_item['product_id'], updated_item['quantity'], item_id)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(updated_item)

# DELETE: Artikel löschen
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM item_list WHERE item_id = %s", (item_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Item deleted"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)  # Port 5003 für den Einkaufswagen-Microservice
