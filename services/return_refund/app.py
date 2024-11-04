# services/return_refund_service/app.py
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

# Return Management

# CREATE: Add a new return
@app.route('/returns', methods=['POST'])
def create_return():
    new_return = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO return_table (ticket_id, date, time, refunds, exchanges) VALUES (%s, %s, %s, %s, %s)",
        (new_return['ticket_id'], new_return['date'], new_return['time'], new_return['refunds'], new_return['exchanges'])
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(new_return), 201

# READ: Retrieve all returns
@app.route('/returns', methods=['GET'])
def get_returns():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM return_table')
    returns = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(returns)

# READ: Retrieve a single return
@app.route('/returns/<int:return_id>', methods=['GET'])
def get_return(return_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM return_table WHERE RTID = %s', (return_id,))
    return_item = cursor.fetchone()
    cursor.close()
    conn.close()

    if return_item:
        return jsonify(return_item)
    return jsonify({"error": "Return not found"}), 404

# UPDATE: Update a return
@app.route('/returns/<int:return_id>', methods=['PUT'])
def update_return(return_id):
    updated_return = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE return_table SET ticket_id = %s, date = %s, time = %s, refunds = %s, exchanges = %s WHERE RTID = %s",
        (updated_return['ticket_id'], updated_return['date'], updated_return['time'], updated_return['refunds'], updated_return['exchanges'], return_id)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(updated_return)

# DELETE: Delete a return
@app.route('/returns/<int:return_id>', methods=['DELETE'])
def delete_return(return_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM return_table WHERE RTID = %s", (return_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Return deleted"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)  # Return & Refund service running on port 5004
