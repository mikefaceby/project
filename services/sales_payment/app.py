# services/sales_payment_service/app.py
from flask import Flask, request, jsonify
from mysql.connector import connect, Error
from config import Config
from datetime import datetime

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

# Helper function to serialize datetime and time fields
def serialize_ticket(ticket):
    for key in ['date', 'time']:
        if ticket.get(key) and isinstance(ticket[key], (datetime,)):
            ticket[key] = ticket[key].isoformat()
    return ticket

# Ticket Management

# CREATE: Add a new ticket
@app.route('/tickets', methods=['POST'])
def create_ticket():
    new_ticket = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO ticket_system (
            date, company_name, time, quantity, subtotal, total, cost, discount, 
            tax, tax_rate, cash, credit, cart_purchase, customer_id, employee_id
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (
            new_ticket['date'], new_ticket.get('company_name'), new_ticket['time'],
            new_ticket['quantity'], new_ticket['subtotal'], new_ticket['total'], 
            new_ticket['cost'], new_ticket.get('discount'), new_ticket['tax'], 
            new_ticket['tax_rate'], new_ticket['cash'], new_ticket['credit'], 
            new_ticket['cart_purchase'], new_ticket.get('customer_id'), 
            new_ticket['employee_id']
        )
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(new_ticket), 201

# READ: Retrieve all tickets
@app.route('/tickets', methods=['GET'])
def get_tickets():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM ticket_system')
    tickets = cursor.fetchall()
    cursor.close()
    conn.close()
    tickets = [serialize_ticket(ticket) for ticket in tickets]
    return jsonify(tickets)

# READ: Retrieve a single ticket
@app.route('/tickets/<int:ticket_id>', methods=['GET'])
def get_ticket(ticket_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM ticket_system WHERE ticket_id = %s', (ticket_id,))
    ticket = cursor.fetchone()
    cursor.close()
    conn.close()

    if ticket:
        return jsonify(serialize_ticket(ticket))
    return jsonify({"error": "Ticket not found"}), 404

# UPDATE: Update a ticket
@app.route('/tickets/<int:ticket_id>', methods=['PUT'])
def update_ticket(ticket_id):
    updated_ticket = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE ticket_system 
        SET date = %s, company_name = %s, time = %s, quantity = %s, 
            subtotal = %s, total = %s, cost = %s, discount = %s, tax = %s, 
            tax_rate = %s, cash = %s, credit = %s, cart_purchase = %s, 
            customer_id = %s, employee_id = %s 
        WHERE ticket_id = %s
        """,
        (
            updated_ticket['date'], updated_ticket.get('company_name'), updated_ticket['time'],
            updated_ticket['quantity'], updated_ticket['subtotal'], updated_ticket['total'], 
            updated_ticket['cost'], updated_ticket.get('discount'), updated_ticket['tax'], 
            updated_ticket['tax_rate'], updated_ticket['cash'], updated_ticket['credit'], 
            updated_ticket['cart_purchase'], updated_ticket.get('customer_id'), 
            updated_ticket['employee_id'], ticket_id
        )
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(updated_ticket)

# DELETE: Delete a ticket
@app.route('/tickets/<int:ticket_id>', methods=['DELETE'])
def delete_ticket(ticket_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM ticket_system WHERE ticket_id = %s", (ticket_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Ticket deleted"})

# Tax Management

# CREATE: Add a new tax record
@app.route('/taxes', methods=['POST'])
def create_tax():
    new_tax = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tax_table (tax_year, state_tax, county_tax, city_rate, tax_rate) VALUES (%s, %s, %s, %s, %s)",
        (new_tax['tax_year'], new_tax['state_tax'], new_tax['county_tax'], new_tax['city_rate'], new_tax['tax_rate'])
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(new_tax), 201

# READ: Retrieve all taxes
@app.route('/taxes', methods=['GET'])
def get_taxes():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM tax_table')
    taxes = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(taxes)

# READ: Retrieve a single tax record
@app.route('/taxes/<int:tax_id>', methods=['GET'])
def get_tax(tax_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM tax_table WHERE TTID = %s', (tax_id,))
    tax = cursor.fetchone()
    cursor.close()
    conn.close()

    if tax:
        return jsonify(tax)
    return jsonify({"error": "Tax not found"}), 404

# UPDATE: Update a tax record
@app.route('/taxes/<int:tax_id>', methods=['PUT'])
def update_tax(tax_id):
    updated_tax = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE tax_table SET tax_year = %s, state_tax = %s, county_tax = %s, city_rate = %s, tax_rate = %s WHERE TTID = %s",
        (updated_tax['tax_year'], updated_tax['state_tax'], updated_tax['county_tax'], updated_tax['city_rate'], updated_tax['tax_rate'], tax_id)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(updated_tax)

# DELETE: Delete a tax record
@app.route('/taxes/<int:tax_id>', methods=['DELETE'])
def delete_tax(tax_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tax_table WHERE TTID = %s", (tax_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Tax deleted"})

# Register Management

# CREATE: Add a new register
@app.route('/registers', methods=['POST'])
def create_register():
    new_register = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO register_table (open_total, close_total, register_num, open_emp_id, close_emp_id, open_time, close_time, drop_time, drop_emp_id, drop_total, note) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (new_register['open_total'], new_register.get('close_total'), new_register['register_num'], new_register['open_emp_id'], new_register.get('close_emp_id'), new_register['open_time'], new_register.get('close_time'), new_register.get('drop_time'), new_register.get('drop_emp_id'), new_register.get('drop_total'), new_register.get('note'))
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(new_register), 201

# READ: Retrieve all registers
@app.route('/registers', methods=['GET'])
def get_registers():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM register_table')
    registers = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(registers)

# READ: Retrieve a single register
@app.route('/registers/<int:register_id>', methods=['GET'])
def get_register(register_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM register_table WHERE register_id = %s', (register_id,))
    register = cursor.fetchone()
    cursor.close()
    conn.close()

    if register:
        return jsonify(register)
    return jsonify({"error": "Register not found"}), 404

# UPDATE: Update a register
@app.route('/registers/<int:register_id>', methods=['PUT'])
def update_register(register_id):
    updated_register = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE register_table SET open_total = %s, close_total = %s, register_num = %s, open_emp_id = %s, close_emp_id = %s, open_time = %s, close_time = %s, drop_time = %s, drop_emp_id = %s, drop_total = %s, note = %s WHERE register_id = %s",
        (updated_register['open_total'], updated_register.get('close_total'), updated_register['register_num'], updated_register['open_emp_id'], updated_register.get('close_emp_id'), updated_register['open_time'], updated_register.get('close_time'), updated_register.get('drop_time'), updated_register.get('drop_emp_id'), updated_register.get('drop_total'), updated_register.get('note'), register_id)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(updated_register)

# DELETE: Delete a register
@app.route('/registers/<int:register_id>', methods=['DELETE'])
def delete_register(register_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM register_table WHERE register_id = %s", (register_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Register deleted"})

# Gift Card Management

# CREATE: Add a new gift card
@app.route('/giftcards', methods=['POST'])
def create_gift_card():
    new_gift_card = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO gift_card (promo_number, card_balance, ticket_id, customer_id) VALUES (%s, %s, %s, %s)",
        (new_gift_card['promo_number'], new_gift_card['card_balance'], new_gift_card.get('ticket_id'), new_gift_card.get('customer_id'))
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(new_gift_card), 201

# READ: Retrieve all gift cards
@app.route('/giftcards', methods=['GET'])
def get_gift_cards():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM gift_card')
    gift_cards = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(gift_cards)

# READ: Retrieve a single gift card
@app.route('/giftcards/<int:gift_id>', methods=['GET'])
def get_gift_card(gift_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM gift_card WHERE gift_id = %s', (gift_id,))
    gift_card = cursor.fetchone()
    cursor.close()
    conn.close()

    if gift_card:
        return jsonify(gift_card)
    return jsonify({"error": "Gift card not found"}), 404

# UPDATE: Update a gift card
@app.route('/giftcards/<int:gift_id>', methods=['PUT'])
def update_gift_card(gift_id):
    updated_gift_card = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE gift_card SET promo_number = %s, card_balance = %s, ticket_id = %s, customer_id = %s WHERE gift_id = %s",
        (updated_gift_card['promo_number'], updated_gift_card['card_balance'], updated_gift_card.get('ticket_id'), updated_gift_card.get('customer_id'), gift_id)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(updated_gift_card)

# DELETE: Delete a gift card
@app.route('/giftcards/<int:gift_id>', methods=['DELETE'])
def delete_gift_card(gift_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM gift_card WHERE gift_id = %s", (gift_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Gift card deleted"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)  # Sales & Payment service running on port 5001
