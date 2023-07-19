from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

def connect_db():
    conn = sqlite3.connect('drugs.db')
    return conn

def get_drugs():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM message')
    rows = cursor.fetchall()
    conn.close()

    drug_list = []
    for row in rows:
        drug_dict = {
            "id": row[0],
            "text": row[1],
            "date": row[2],
            "username": row[3],
        }
        drug_list.append(drug_dict)

    return drug_list

def save_chat_message(message):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO message (text, date, username) VALUES (?, ?, ?)', (message['text'], message['date'], message['username']))
    conn.commit()
    conn.close()

@app.route('/api/drug', methods=['GET'])
def get_drug_data():
    drugs = get_drugs()
    return jsonify(drugs)

@app.route('/api/drug', methods=['POST'])
def handle_chat_message():
    message = request.get_json()
    save_chat_message(message)
    return jsonify({'message': 'メッセージが保存されました。'})

if __name__ == '__main__':
    app.run(debug=True)
