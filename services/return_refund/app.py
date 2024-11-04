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

# Rückgabeverwaltung

# CREATE: Neue Rückgabe hinzufügen
@app.route('/returns', methods=['POST'])
def create_return():
    new_return = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO return_table (return_id, ticket_id, return_date, reason) VALUES (%s, %s, %s, %s)",
        (new_return['return_id'], new_return['ticket_id'], new_return['return_date'], new_return['reason'])
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(new_return), 201

# READ: Alle Rückgaben abrufen
@app.route('/returns', methods=['GET'])
def get_returns():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM return_table')
    returns = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(returns)

# READ: Einzelne Rückgabe abrufen
@app.route('/returns/<int:return_id>', methods=['GET'])
def get_return(return_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM return_table WHERE return_id = %s', (return_id,))
    return_item = cursor.fetchone()
    cursor.close()
    conn.close()

    if return_item:
        return jsonify(return_item)
    return jsonify({"error": "Return not found"}), 404

# UPDATE: Rückgabe aktualisieren
@app.route('/returns/<int:return_id>', methods=['PUT'])
def update_return(return_id):
    updated_return = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE return_table SET ticket_id = %s, return_date = %s, reason = %s WHERE return_id = %s",
        (updated_return['ticket_id'], updated_return['return_date'], updated_return['reason'], return_id)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(updated_return)

# DELETE: Rückgabe löschen
@app.route('/returns/<int:return_id>', methods=['DELETE'])
def delete_return(return_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM return_table WHERE return_id = %s", (return_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Return deleted"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)  # Externer Port für den Service
