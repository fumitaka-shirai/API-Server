from flask import Flask, jsonify,request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

def get_detiles():
    conn = sqlite3.connect('drugs.db')
    conn.row_factory = dict_factory
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM detiles')

    detiles = cursor.fetchall()
    conn.close()

    return detiles 
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
    for idx, row in enumerate(drug):
        drug_id = idx + 1  
        drug_dict = {
            "id": drug_id,
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
    cursor.execute('SELECT * FROM chat')
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
    drug_id = data.get('drug_id')  

    cursor.execute("INSERT INTO chat (text, date, username, drug_id) VALUES (?, ?, ?, ?)", (text, date, username, drug_id))
    conn.commit()
    message_id = cursor.lastrowid

    conn.close()

    message = {
        'id': message_id,
        'text': text,
        'date': date,
        'username': username,
        'drug_id': drug_id  
    }
    return jsonify(message)

@app.route('/api/detiles', methods=['GET'])
def get_detiles():
    conn = sqlite3.connect('drugs.db')
    conn.row_factory = dict_factory
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM detiles')

    detiles = cursor.fetchall()
    conn.close()

    detiles_list = []  # リストを初期化

    for data in detiles:  # リスト内の各データを個別に処理
        detile = {
            'id': data['id'],
            'name': data['name'],
            'indication': data['indication'],
            'interations': data['interations'],
            'sideeffects': data['sideeffects'],
            'pharmacology': data['pharmacology'],
            'drug_id': data['drug_id']
        }
        detiles_list.append(detile)

    if detiles_list:
        # 薬の詳細情報が見つかった場合はJSON形式に整形して返す
        return jsonify(detiles_list)
    else:
        # データが見つからなかった場合はエラーを返す
        return jsonify({'error': 'Detiles not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
