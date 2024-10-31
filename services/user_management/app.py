# services/user_service/app.py
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

# GET: Retrieve all users
@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM customer_info')
    users = cursor.fetchall()
    conn.close()
    return jsonify(users)

# POST: Create a new user
@app.route('/user', methods=['POST'])
def create_user():
    new_user = request.get_json()
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO customer_info (customer_id, name) VALUES (%s, %s)",
        (new_user['customer_id'], new_user['name'])
    )
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify(new_user), 201

# GET: Retrieve user information
@app.route('/user/<int:customer_id>', methods=['GET'])
def get_user(customer_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM customer_info WHERE customer_id = %s", (customer_id,))
    user = cursor.fetchone()
    cursor.close()
    connection.close()

    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# PUT: Update user information
@app.route('/user/<int:customer_id>', methods=['PUT'])
def update_user(customer_id):
    updated_user = request.get_json()
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE customer_info SET name = %s WHERE customer_id = %s",
        (updated_user['name'], customer_id)
    )
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify(updated_user)

# DELETE: Delete a user
@app.route('/user/<int:customer_id>', methods=['DELETE'])
def delete_user(customer_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM customer_info WHERE customer_id = %s", (customer_id,))
    connection.commit()
    cursor.close()
    connection.close()

    return jsonify({"message": "User deleted"})

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
