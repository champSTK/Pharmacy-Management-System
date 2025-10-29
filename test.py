import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="sqlserver@123",
        database="mydata"
    )

    if conn.is_connected():
        print("Connected to MySQL database")

        cursor = conn.cursor()
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        print("Tables in database:", tables)  # Debugging

        cursor.execute("SELECT * FROM pharma")
        rows = cursor.fetchall()

        if rows:
            print("Data in 'pharma' table:")
            for row in rows:
                print(row)
        else:
            print("No data found in 'pharma' table.")

except Error as e:
    print(f"Error: {e}")

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("Connection closed.")
