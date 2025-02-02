import os
import shutil
import pandas as pd
from flask import Flask, render_template, request, send_file, jsonify

# Configuration
OUTPUT_DIR = "output"
STATIC_DIR = "static_site"

# Ensure required directories exist
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(STATIC_DIR, exist_ok=True)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/convert", methods=["POST"])
def convert():
    """Handle file upload and conversion"""
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    try:
        df = pd.read_csv(file)
        excel_filename = os.path.join(OUTPUT_DIR, "converted.xlsx")
        df.to_excel(excel_filename, index=False, engine='openpyxl')

        return send_file(excel_filename, as_attachment=True)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# **New Function: Export Static Files for GitHub Pages**
def export_static_files():
    """Copies HTML, CSS, and JS files to a static site folder."""
    if os.path.exists(STATIC_DIR):
        shutil.rmtree(STATIC_DIR)  # Remove existing folder
    os.makedirs(STATIC_DIR, exist_ok=True)

    # Copy static assets
    shutil.copytree("static", os.path.join(STATIC_DIR, "static"))
    shutil.copytree("templates", os.path.join(STATIC_DIR, "templates"))

    # Copy the main HTML file
    shutil.copy("templates/index.html", os.path.join(STATIC_DIR, "index.html"))

    print("✅ Static files exported successfully!")

if __name__ == "__main__":
    if os.getenv("GITHUB_ACTIONS") == "true":
        export_static_files()  # Run this ONLY inside GitHub Actions
    else:
        app.run(debug=True)
