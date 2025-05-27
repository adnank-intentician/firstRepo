from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3
from database import init_db


app = Flask(__name__)
CORS(app)
init_db()

def get_db():
    conn = sqlite3.connect('fruits.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/click/<fruit>",methods=['POST'])
def click_fruit(fruit):
    conn = get_db()
    conn.execute("UPDATE fruit_clicks SET count= count+1  WHERE fruit = ? ",(fruit,))
    conn.commit()
    conn.close()
    return jsonify({"message":f"{fruit} clicked"})

@app.route("/counts",methods=["GET"])
def get_counts():
    conn = get_db()
    rows = conn.execute("SELECT * FROM fruit_clicks").fetchall()
    conn.close()
    return jsonify({row["fruit"]: row["count"] for row in rows})



if __name__=='__main__':
    app.run(debug=False,port=5000)


