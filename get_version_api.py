from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# Database configuration
db_config = {
    "host": "localhost",
    "user": "sairam",  # Change to your MySQL username
    "password": "sairam@2001",  # Change to your MySQL password
    "database": "demo"
}

# API endpoint to fetch users
@app.route('/versions', methods=['GET'])
def get_users():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)  # Enables fetching results as dictionaries
        cursor.execute("SELECT * FROM demo_app_versions")
        versions = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(versions)  # Return data as JSON response
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Return error if something goes wrong

if __name__ == '__main__':
    app.run(debug=True)

