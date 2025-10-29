🏥 Pharmacy Management System (Python + Tkinter + MySQL)

A simple and user-friendly Pharmacy Management System built using Python (Tkinter GUI) with MySQL database for storing and managing medicine records.
This project allows users to add, update, search, and delete medicine details with a clean interface.

📌 Features

✅ Add New Medicine with Reference Number
✅ Prevent Duplicate Reference Numbers
✅ Store & Manage Medicine Details
✅ Search Medicines Using Filters
✅ Update and Delete Records
✅ Auto Refresh Tables after Data Operations
✅ Error Handling for Database Operations
✅ Fully Responsive Tkinter GUI

🧠 How It Works

The application connects to a MySQL database and allows the user to manage pharmacy records.
Users can enter medicine details, save them to the database, and view them instantly in the UI.
Built-in validations ensure no duplicate reference numbers are inserted and required fields must be filled.

🛠️ Tech Stack
Component	Technology
Programming Language	Python
GUI Framework	Tkinter
Database	MySQL
DB Connector	mysql-connector-python
📂 Database Setup

Create a database named mydata and the following tables:

Table 1: pharma – for storing medicine details
Column
<img width="170" height="25" alt="image" src="https://github.com/user-attachments/assets/3684f4ef-f531-4a32-a03f-c6a2d90b7a39" />

Table 2: pharmacy – for storing main pharmacy records
Column
<img width="1094" height="23" alt="image" src="https://github.com/user-attachments/assets/1795506d-a35d-43a2-a26c-a3d2630311a8" />


🚀 Running the Project
1️⃣ Install Required Python Modules
pip install mysql-connector-python

2️⃣ Run MySQL and Create Database

Make sure MySQL Server is running.

3️⃣ Update Your SQL Password in Code

IMPORTANT:
You MUST update the MySQL password inside the Python code before running, otherwise the program will not connect to the database.

Open the code and update this part with your own MySQL password:

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_MYSQL_PASSWORD_HERE",   # ← Change this
    database="mydata"
)

4️⃣ Run the Program
python main.py
