from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app) 

@app.route('/drug', methods=['GET'])
def get_drug():
    conn = sqlite3.connect('drug.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM drug')
    drugs = cursor.fetchall()
    conn.close()
    return jsonify(drugs)

if __name__ == '__main__':
    app.run(debug=True)
