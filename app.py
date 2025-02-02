from flask import Flask, render_template, request, send_file, jsonify
import pandas as pd
import os

class Config:
    OUTPUT_DIR = "output"
    STATIC_DIR = "static_site"

    @staticmethod
    def ensure_directories():
        os.makedirs(Config.OUTPUT_DIR, exist_ok=True)
        os.makedirs(Config.STATIC_DIR, exist_ok=True)

Config.ensure_directories()

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
        excel_filename = os.path.join(Config.OUTPUT_DIR, "converted.xlsx")
        df.to_excel(excel_filename, index=False, engine='openpyxl')

        return send_file(excel_filename, as_attachment=True)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)