# services/sales_payment/app.py
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
# Verkaufsverwaltung

# CREATE: Neues Ticket hinzufügen
@app.route('/tickets', methods=['POST'])
def create_ticket():
    new_ticket = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO ticket_system (ticket_id, sale_date, total_amount) VALUES (%s, %s, %s)",
        (new_ticket['ticket_id'], new_ticket['sale_date'], new_ticket['total_amount'])
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(new_ticket), 201

# READ: Alle Tickets abrufen
@app.route('/tickets', methods=['GET'])
def get_tickets():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM ticket_system')
    tickets = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(tickets)

# READ: Einzelnes Ticket abrufen
@app.route('/tickets/<int:ticket_id>', methods=['GET'])
def get_ticket(ticket_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM ticket_system WHERE ticket_id = %s', (ticket_id,))
    ticket = cursor.fetchone()
    cursor.close()
    conn.close()

    if ticket:
        return jsonify(ticket)
    return jsonify({"error": "Ticket not found"}), 404

# UPDATE: Ticket aktualisieren
@app.route('/tickets/<int:ticket_id>', methods=['PUT'])
def update_ticket(ticket_id):
    updated_ticket = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE ticket_system SET sale_date = %s, total_amount = %s WHERE ticket_id = %s",
        (updated_ticket['sale_date'], updated_ticket['total_amount'], ticket_id)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(updated_ticket)

# DELETE: Ticket löschen
@app.route('/tickets/<int:ticket_id>', methods=['DELETE'])
def delete_ticket(ticket_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM ticket_system WHERE ticket_id = %s", (ticket_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Ticket deleted"})

# Steuerverwaltung

# CREATE: Neue Steuer hinzufügen
@app.route('/taxes', methods=['POST'])
def create_tax():
    new_tax = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tax_table (tax_id, tax_rate) VALUES (%s, %s)",
        (new_tax['tax_id'], new_tax['tax_rate'])
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(new_tax), 201

# READ: Alle Steuern abrufen
@app.route('/taxes', methods=['GET'])
def get_taxes():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM tax_table')
    taxes = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(taxes)

# READ: Einzelne Steuer abrufen
@app.route('/taxes/<int:tax_id>', methods=['GET'])
def get_tax(tax_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM tax_table WHERE tax_id = %s', (tax_id,))
    tax = cursor.fetchone()
    cursor.close()
    conn.close()

    if tax:
        return jsonify(tax)
    return jsonify({"error": "Tax not found"}), 404

# UPDATE: Steuer aktualisieren
@app.route('/taxes/<int:tax_id>', methods=['PUT'])
def update_tax(tax_id):
    updated_tax = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE tax_table SET tax_rate = %s WHERE tax_id = %s",
        (updated_tax['tax_rate'], tax_id)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(updated_tax)

# DELETE: Steuer löschen
@app.route('/taxes/<int:tax_id>', methods=['DELETE'])
def delete_tax(tax_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tax_table WHERE tax_id = %s", (tax_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Tax deleted"})

# Kassenverwaltung

# CREATE: Neue Registrierkasse hinzufügen
@app.route('/registers', methods=['POST'])
def create_register():
    new_register = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO registers_table (register_id, location, is_open) VALUES (%s, %s, %s)",
        (new_register['register_id'], new_register['location'], new_register['is_open'])
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(new_register), 201

# READ: Alle Registrierkassen abrufen
@app.route('/registers', methods=['GET'])
def get_registers():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM registers_table')
    registers = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(registers)

# READ: Einzelne Registrierkasse abrufen
@app.route('/registers/<int:register_id>', methods=['GET'])
def get_register(register_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM registers_table WHERE register_id = %s', (register_id,))
    register = cursor.fetchone()
    cursor.close()
    conn.close()

    if register:
        return jsonify(register)
    return jsonify({"error": "Register not found"}), 404

# UPDATE: Registrierkasse aktualisieren
@app.route('/registers/<int:register_id>', methods=['PUT'])
def update_register(register_id):
    updated_register = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE registers_table SET location = %s, is_open = %s WHERE register_id = %s",
        (updated_register['location'], updated_register['is_open'], register_id)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(updated_register)

# DELETE: Registrierkasse löschen
@app.route('/registers/<int:register_id>', methods=['DELETE'])
def delete_register(register_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM registers_table WHERE register_id = %s", (register_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Register deleted"})

# Geschenkkartenverwaltung

# CREATE: Neue Geschenkkarte hinzufügen
@app.route('/giftcards', methods=['POST'])
def create_gift_card():
    new_gift_card = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO gift_card (card_id, balance) VALUES (%s, %s)",
        (new_gift_card['card_id'], new_gift_card['balance'])
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(new_gift_card), 201

# READ: Alle Geschenkkarten abrufen
@app.route('/giftcards', methods=['GET'])
def get_gift_cards():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM gift_card')
    gift_cards = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(gift_cards)

# READ: Einzelne Geschenkkarte abrufen
@app.route('/giftcards/<int:card_id>', methods=['GET'])
def get_gift_card(card_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM gift_card WHERE card_id = %s', (card_id,))
    gift_card = cursor.fetchone()
    cursor.close()
    conn.close()

    if gift_card:
        return jsonify(gift_card)
    return jsonify({"error": "Gift card not found"}), 404

# UPDATE: Geschenkkarte aktualisieren
@app.route('/giftcards/<int:card_id>', methods=['PUT'])
def update_gift_card(card_id):
    updated_gift_card = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE gift_card SET balance = %s WHERE card_id = %s",
        (updated_gift_card['balance'], card_id)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(updated_gift_card)

# DELETE: Geschenkkarte löschen
@app.route('/giftcards/<int:card_id>', methods=['DELETE'])
def delete_gift_card(card_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM gift_card WHERE card_id = %s", (card_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Gift card deleted"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)  # Externer Port für den Service
