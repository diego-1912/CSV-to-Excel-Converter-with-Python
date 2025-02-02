from flask import Flask, render_template, request, send_file
import pandas as pd
import os

app = Flask(__name__)

# Ensure the output directory exists
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/convert", methods=["POST"])
def convert():
    """Handle file upload and conversion"""
    if "file" not in request.files:
        return "No file uploaded", 400

    file = request.files["file"]

    if file.filename == "":
        return "No selected file", 400

    try:
        df = pd.read_csv(file)
        excel_filename = os.path.join(OUTPUT_DIR, "converted.xlsx")
        df.to_excel(excel_filename, index=False, engine='openpyxl')

        return send_file(excel_filename, as_attachment=True)

    except Exception as e:
        return str(e), 500

if __name__ == "__main__":
    app.run(debug=True)

