from flask import Flask, jsonify,request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d 

def connect_db():
    conn = sqlite3.connect('drugs.db')
    return conn

@app.route('/api/drug', methods=['GET'])
def get_drug():
    conn = sqlite3.connect('drugs.db')
    conn.row_factory = dict_factory
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM drugs')
    drug = cursor.fetchall()
    conn.close()
    

    drug_list = []
    for row in drug:
        drug_dict = {
            "Category": row['category'],
            "Name": row['name'],
            "Dose": row['dose'],
        }
        drug_list.append(drug_dict)

    return jsonify(drug_list)


@app.route('/api/chat', methods=['GET'])
def get_chat():
    conn = connect_db()
    conn.row_factory = dict_factory
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM message')
    messages = cursor.fetchall()
    conn.close()

    return jsonify(messages)

@app.route('/api/chat', methods=['POST'])
def add_chat():
    conn = connect_db()
    cursor = conn.cursor()
    data = request.json
    text = data.get('text')
    date = data.get('date')
    username = data.get('username')

    cursor.execute("INSERT INTO message (text, date, username) VALUES (?, ?, ?)", (text, date, username))
    conn.commit()
    message_id = cursor.lastrowid

    conn.close()

    message = {
        'id': message_id,
        'text': text,
        'date': date,
        'username': username
    }
    return jsonify(message)

if __name__ == '__main__':
    app.run(debug=True)
