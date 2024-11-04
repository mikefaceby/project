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

# GET: Retrieve all customers
@app.route('/customers', methods=['GET'])
def get_customers():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM customer_info')
    customers = cursor.fetchall()
    conn.close()
    return jsonify(customers)

# POST: Create a new customer
@app.route('/customers', methods=['POST'])
def create_customer():
    new_customer = request.get_json()
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO customer_info (customer_id, name) VALUES (%s, %s)",
        (new_customer['customer_id'], new_customer['name'])
    )
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify(new_customer), 201

# GET: Retrieve customer information
@app.route('/customers/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM customer_info WHERE customer_id = %s", (customer_id,))
    customer = cursor.fetchone()
    cursor.close()
    connection.close()

    if customer:
        return jsonify(customer)
    return jsonify({"error": "Customer not found"}), 404

# PUT: Update customer information
@app.route('/customers/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    updated_customer = request.get_json()
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE customer_info SET name = %s WHERE customer_id = %s",
        (updated_customer['name'], customer_id)
    )
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify(updated_customer)

# DELETE: Delete a customer
@app.route('/customers/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM customer_info WHERE customer_id = %s", (customer_id,))
    connection.commit()
    cursor.close()
    connection.close()

    return jsonify({"message": "Customer deleted"})

# POST: Create a new employee
@app.route('/employee', methods=['POST'])
def create_employee():
    new_employee = request.get_json()
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO employee_info (employee_id, name) VALUES (%s, %s)",
        (new_employee['employee_id'], new_employee['name'])
    )
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify(new_employee), 201

# GET: Retrieve employee information
@app.route('/employee/<int:employee_id>', methods=['GET'])
def get_employee(employee_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM employee_info WHERE employee_id = %s", (employee_id,))
    employee = cursor.fetchone()
    cursor.close()
    connection.close()

    if employee:
        return jsonify(employee)
    return jsonify({"error": "Employee not found"}), 404

# PUT: Update employee information
@app.route('/employee/<int:employee_id>', methods=['PUT'])
def update_employee(employee_id):
    updated_employee = request.get_json()
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE employee_info SET name = %s WHERE employee_id = %s",
        (updated_employee['name'], employee_id)
    )
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify(updated_employee)

# DELETE: Delete an employee
@app.route('/employee/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM employee_info WHERE employee_id = %s", (employee_id,))
    connection.commit()
    cursor.close()
    connection.close()

    return jsonify({"message": "Employee deleted"})

# POST: Create a new store
@app.route('/store', methods=['POST'])
def create_store():
    new_store = request.get_json()
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO stores (store_id, name, location) VALUES (%s, %s, %s)",
        (new_store['store_id'], new_store['name'], new_store['location'])
    )
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify(new_store), 201

# GET: Retrieve store information
@app.route('/store/<int:store_id>', methods=['GET'])
def get_store(store_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM stores WHERE store_id = %s", (store_id,))
    store = cursor.fetchone()
    cursor.close()
    connection.close()

    if store:
        return jsonify(store)
    return jsonify({"error": "Store not found"}), 404

# PUT: Update store information
@app.route('/store/<int:store_id>', methods=['PUT'])
def update_store(store_id):
    updated_store = request.get_json()
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE stores SET name = %s, location = %s WHERE store_id = %s",
        (updated_store['name'], updated_store['location'], store_id)
    )
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify(updated_store)

# DELETE: Delete a store
@app.route('/store/<int:store_id>', methods=['DELETE'])
def delete_store(store_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM stores WHERE store_id = %s", (store_id,))
    connection.commit()
    cursor.close()
    connection.close()

    return jsonify({"message": "Store deleted"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # User-Service läuft auf Port 5000
