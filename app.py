# app.py
import mysql.connector
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/data')
def data():
    conn = mysql.connector.connect(
        host="mysql-db",  # Use the OpenShift service name
        user="flaskuser",
        password="flaskpassword",
        database="flaskdb"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM example_table;")
    result = cursor.fetchall()
    return jsonify(result)

@app.route('/data')
def data():
    return jsonify({"data": ["item1", "item2", "item3"]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
