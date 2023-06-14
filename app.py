from flask import Flask, jsonify, render_template
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

@app.route('/api/drug', methods=['GET'])
def get_drug():
    conn = sqlite3.connect('drug.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM drug')
    drug = cursor.fetchall()
    conn.close()

    drug_list = []
    for row in drug:
        drug_dict = {
            "Category": row[1],
            "Name": row[2],
            "Dose": row[3],
            "Taste": row[4]
        }
        drug_list.append(drug_dict)

    return jsonify(drug_list)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
