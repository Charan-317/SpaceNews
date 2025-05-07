from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route("/post_blog", methods=["POST"])
def post_blog():
    data = request.json
    conn = sqlite3.connect("blogs.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO blogs (title, content) VALUES (?, ?)", (data["title"], data["content"]))
    conn.commit()
    conn.close()
    return jsonify({"message": "Blog posted successfully!"})

@app.route("/get_blogs", methods=["GET"])
def get_blogs():
    conn = sqlite3.connect("blogs.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM blogs")
    blogs = cursor.fetchall()
    conn.close()
    return jsonify(blogs)

if __name__ == "__main__":
    app.run(debug=True)
