from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Database Configuration
db_config = {
    "host": "localhost",
    "user": "sairam",  # Change to your MySQL username
    "password": "sairam@2001",  # Change to your MySQL password
    "database": "demo"
}

# API to insert a new user
@app.route('/add_version', methods=['POST'])
def add_user():
    try:
        data = request.json  # Get JSON data from request
        app_name = data.get("app_name")
        app_link = data.get("app_link")
        release_date = data.get("release_date")
        release_note = data.get("release_note")
        is_in_playstore = data.get("is_in_playstore")

        if not app_name or not app_link or not release_date or not release_note or not is_in_playstore:
            return jsonify({"error": "app_name and app_link and all fileds are mandatory"}), 400

        # Connect to MySQL and insert data
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO demo_app_versions (app_name,app_link,release_date,release_note,is_in_playstore) VALUES (%s, %s ,%s ,%s, %s)", (app_name, app_link,release_date,release_note,is_in_playstore))
        conn.commit()

        cursor.close()
        conn.close()

        return jsonify({"message": "version added sucessfully"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
