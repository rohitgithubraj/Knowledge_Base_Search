from flask import Flask, request, jsonify, send_from_directory
import sqlite3
import os

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def serve_index():
    return send_from_directory(BASE_DIR, "index.html")

@app.route("/<path:path>")
def static_files(path):
    return send_from_directory(BASE_DIR, path)

@app.route("/search")
def search():
    query = request.args.get("query", "")
    conn = sqlite3.connect('knowledge_base.db')
    cursor = conn.cursor()
    cursor.execute("SELECT title, url FROM knowledge WHERE title LIKE ?", (f"%{query}%",))
    results = [{"title": title, "url": url} for title, url in cursor.fetchall()]
    conn.close()
    return jsonify(results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
