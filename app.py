from flask import Flask, jsonify, render_template
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d 
@app.route('/api/drug', methods=['GET'])
def get_drug():
    conn = sqlite3.connect('drug.db')
    conn.row_factory = dict_factory
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM drug')
    drug = cursor.fetchall()
    conn.close()

    drug_list = []
    for row in drug:
        drug_dict = {
            "Category": row['category'],
            "Name": row['name'],
            "Dose": row['dose'],
            "Taste": row['taste']
        }
        drug_list.append(drug_dict)

    return jsonify(drug_list)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
