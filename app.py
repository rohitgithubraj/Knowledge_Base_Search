from flask import Flask, request, jsonify, send_from_directory
import sqlite3

app = Flask(__name__)

@app.route("/")
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route("/<path:path>")
def static_files(path):
    return send_from_directory('.', path)
 
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
    app.run(debug=True)
