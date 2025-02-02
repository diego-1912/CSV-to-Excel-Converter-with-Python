
# CSV to Excel Converter (Web-Based)

## 📌 Project Objective
This project provides a **web-based UI** for converting CSV files into Excel files using **Flask, Pandas, and OpenPyXL**. Users can upload a CSV file and download the converted Excel file through a modern, user-friendly web interface.

---

## 📦 Dependencies & Required Libraries
Ensure you have the following dependencies installed before running the project:

| Package    | Purpose |
|------------|---------|
| Flask      | Web framework for creating the UI |
| Pandas     | For reading and processing CSV files |
| OpenPyXL   | To generate Excel files from CSV |
| HTML/CSS/JS | Frontend for user interaction |

Install the dependencies using:
```sh
pip install flask pandas openpyxl
```

---

## 📁 Folder Structure
```
csv_to_excel_converter/
│── static/                   # Static files for styling and interactivity
│   ├── styles.css            # CSS for UI design
│   ├── script.js             # JavaScript for handling file uploads
│── templates/                # HTML templates for Flask
│   ├── index.html            # Main webpage
│── output/                   # Stores converted Excel files
│── app.py                    # Flask backend script
│── requirements.txt           # List of dependencies
│── README.md                  # Documentation file
```

---

## 🚀 How to Run the Project

### **Step 1: Install Python**
Ensure you have Python **3.7 or later** installed. Check your Python version:
```sh
python --version
```

### **Step 2: Clone the Repository**
If using Git:
```sh
git clone https://github.com/yourusername/csv_to_excel_converter.git
cd csv_to_excel_converter
```
Otherwise, manually download the files and navigate to the folder.

### **Step 3: Install Dependencies**
Run the following command in your terminal:
```sh
pip install -r requirements.txt
```

### **Step 4: Start the Flask Server**
Run the Flask application:
```sh
python app.py
```
If Flask is not found, try:
```sh
python -m flask run
```

### **Step 5: Open the Web App**
Once the server is running, open your browser and go to:
```
http://127.0.0.1:5000/
```

### **Step 6: Convert Files**
1. Click **"Choose File"** and select a CSV file.
2. Click **"Convert & Download"** to download the converted Excel file.

---

## 🔧 Troubleshooting
- If `ModuleNotFoundError: No module named 'flask'`, run:
  ```sh
  pip install flask
  ```
- If Flask server doesn’t start, ensure you are inside the correct project folder:
  ```sh
  cd csv_to_excel_converter
  python app.py
  ```
- If `permission denied` on Mac/Linux, try:
  ```sh
  chmod +x app.py
  python app.py
  ```

---

## 💡 Future Improvements
- Add file format validation before conversion.
- Implement a progress bar for large files.
- Deploy the app to **Heroku** or **AWS** for online use.

---

### 🎯 **Author**
📌 Created by **Your Name**  
📧 Contact: [your.email@example.com](mailto:your.email@example.com)  

---

**Enjoy using the CSV to Excel Converter! 🚀**
```

