from flask import Flask, jsonify, send_from_directory, render_template
import os

app = Flask(__name__)

COURSE_FOLDERS = {
    "dynamics": r"C:\Users\aridb\Documents\University of Wisconsin-Madison\fall 2025\E M A 202",
    "mom": r"C:\Users\aridb\Documents\University of Wisconsin-Madison\fall 2025\E M A 303",
    "tutor": r"C:\Users\aridb\Documents\University of Wisconsin-Madison\fall 2025\ED POL 150",
    "vcc": r"C:\Users\aridb\Documents\University of Wisconsin-Madison\fall 2025\MATH 321",
    "thermo": r"C:\Users\aridb\Documents\University of Wisconsin-Madison\fall 2025\M E 361",
    "lab": r"C:\Users\aridb\Documents\University of Wisconsin-Madison\fall 2025\E M A 307",
    "num": r"C:\Users\aridb\Documents\University of Wisconsin-Madison\fall 2025\MATH 467"
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/files/<course>")
def list_files(course):
    if course not in COURSE_FOLDERS:
        return jsonify({"error": "Invalid course"}), 404

    folder = COURSE_FOLDERS[course]
    if not os.path.exists(folder):
        return jsonify([])

    files = os.listdir(folder)
    return jsonify(files)

@app.route("/files/<course>/<filename>")
def get_file(course, filename):
    if course not in COURSE_FOLDERS:
        return "Invalid course", 404
    folder = COURSE_FOLDERS[course]
    return send_from_directory(folder, filename)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
