# services/user_service/app.py
from flask import Flask, request, jsonify
from mysql.connector import connect, Error
from config import Config

app = Flask(__name__)

# Establishing database connection
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
    try:
        conn = get_db_connection()
        if conn is None:
            return jsonify({"error": "Database connection failed"}), 500
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM customer_info')
        customers = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(customers)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# POST: Create a new customer
@app.route('/customers', methods=['POST'])
def create_customer():
    try:
        new_customer = request.get_json()
        connection = get_db_connection()
        if connection is None:
            return jsonify({"error": "Database connection failed"}), 500
        cursor = connection.cursor()
        cursor.execute(
            """
            INSERT INTO customer_info (
                email, password, first_name, last_name, 
                phone_number, rewards, street_address, city, 
                state, zip_code
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                new_customer['email'],
                new_customer['password'],
                new_customer['first_name'],
                new_customer['last_name'],
                new_customer['phone_number'],
                new_customer['rewards'],
                new_customer['street_address'],
                new_customer['city'],
                new_customer['state'],
                new_customer['zip_code']
            )
        )
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify(new_customer), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# GET: Retrieve customer information
@app.route('/customers/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    try:
        connection = get_db_connection()
        if connection is None:
            return jsonify({"error": "Database connection failed"}), 500
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM customer_info WHERE customer_id = %s", (customer_id,))
        customer = cursor.fetchone()
        cursor.close()
        connection.close()

        if customer:
            return jsonify(customer)
        return jsonify({"error": "Customer not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# PUT: Update customer information
@app.route('/customers/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    try:
        updated_customer = request.get_json()
        connection = get_db_connection()
        if connection is None:
            return jsonify({"error": "Database connection failed"}), 500
        cursor = connection.cursor()
        cursor.execute(
            """
            UPDATE customer_info 
            SET email = %s, password = %s, first_name = %s, last_name = %s, 
                phone_number = %s, rewards = %s, street_address = %s, 
                city = %s, state = %s, zip_code = %s 
            WHERE customer_id = %s
            """,
            (
                updated_customer['email'],
                updated_customer['password'],
                updated_customer['first_name'],
                updated_customer['last_name'],
                updated_customer['phone_number'],
                updated_customer['rewards'],
                updated_customer['street_address'],
                updated_customer['city'],
                updated_customer['state'],
                updated_customer['zip_code'],
                customer_id
            )
        )
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify(updated_customer)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# DELETE: Delete a customer
@app.route('/customers/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    try:
        connection = get_db_connection()
        if connection is None:
            return jsonify({"error": "Database connection failed"}), 500
        cursor = connection.cursor()
        cursor.execute("DELETE FROM customer_info WHERE customer_id = %s", (customer_id,))
        connection.commit()
        cursor.close()
        connection.close()

        return jsonify({"message": "Customer deleted"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# POST: Create a new employee
@app.route('/employee', methods=['POST'])
def create_employee():
    try:
        new_employee = request.get_json()
        connection = get_db_connection()
        if connection is None:
            return jsonify({"error": "Database connection failed"}), 500
        cursor = connection.cursor()
        cursor.execute(
            """
            INSERT INTO employee_info (
                email, password, pin_number, first_name, last_name, 
                user_id, phone_number, SSN, street_address, city, 
                state, zip_code, start_date, company_name, 
                number_of_stores, user_type, customer_id
            ) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                new_employee['email'],
                new_employee['password'],
                new_employee.get('pin_number'),
                new_employee['first_name'],
                new_employee['last_name'],
                new_employee.get('user_id'),
                new_employee['phone_number'],
                new_employee.get('SSN'),
                new_employee['street_address'],
                new_employee['city'],
                new_employee['state'],
                new_employee['zip_code'],
                new_employee.get('start_date'),
                new_employee['company_name'],
                new_employee.get('number_of_stores'),
                new_employee['user_type'],
                new_employee.get('customer_id')
            )
        )
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify(new_employee), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# GET: Retrieve employee information
@app.route('/employee/<int:employee_id>', methods=['GET'])
def get_employee(employee_id):
    try:
        connection = get_db_connection()
        if connection is None:
            return jsonify({"error": "Database connection failed"}), 500
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM employee_info WHERE employee_id = %s", (employee_id,))
        employee = cursor.fetchone()
        cursor.close()
        connection.close()

        if employee:
            return jsonify(employee)
        return jsonify({"error": "Employee not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# PUT: Update employee information
@app.route('/employee/<int:employee_id>', methods=['PUT'])
def update_employee(employee_id):
    try:
        updated_employee = request.get_json()
        connection = get_db_connection()
        if connection is None:
            return jsonify({"error": "Database connection failed"}), 500
        cursor = connection.cursor()
        cursor.execute(
            """
            UPDATE employee_info 
            SET email = %s, password = %s, pin_number = %s, first_name = %s, 
                last_name = %s, user_id = %s, phone_number = %s, SSN = %s, 
                street_address = %s, city = %s, state = %s, zip_code = %s, 
                start_date = %s, company_name = %s, number_of_stores = %s, 
                user_type = %s, customer_id = %s 
            WHERE employee_id = %s
            """,
            (
                updated_employee['email'],
                updated_employee['password'],
                updated_employee.get('pin_number'),
                updated_employee['first_name'],
                updated_employee['last_name'],
                updated_employee.get('user_id'),
                updated_employee['phone_number'],
                updated_employee.get('SSN'),
                updated_employee['street_address'],
                updated_employee['city'],
                updated_employee['state'],
                updated_employee['zip_code'],
                updated_employee.get('start_date'),
                updated_employee['company_name'],
                updated_employee.get('number_of_stores'),
                updated_employee['user_type'],
                updated_employee.get('customer_id'),
                employee_id
            )
        )
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify(updated_employee)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# DELETE: Delete an employee
@app.route('/employee/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    try:
        connection = get_db_connection()
        if connection is None:
            return jsonify({"error": "Database connection failed"}), 500
        cursor = connection.cursor()
        cursor.execute("DELETE FROM employee_info WHERE employee_id = %s", (employee_id,))
        connection.commit()
        cursor.close()
        connection.close()

        return jsonify({"message": "Employee deleted"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# POST: Create a new store
@app.route('/store', methods=['POST'])
def create_store():
    try:
        new_store = request.get_json()
        connection = get_db_connection()
        if connection is None:
            return jsonify({"error": "Database connection failed"}), 500
        cursor = connection.cursor()
        cursor.execute(
            """
            INSERT INTO stores (SID, company_name, employee_id)
            VALUES (%s, %s, %s)
            """,
            (new_store['SID'], new_store['company_name'], new_store['employee_id'])
        )
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify(new_store), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # User-Service läuft auf Port 5000
