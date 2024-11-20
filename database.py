import pymysql
from tkinter import messagebox

def connection_database():
    try:
        connection = pymysql.connect(host="localhost", user="root", password="9398")
        with connection.cursor() as cursor:
            cursor.execute("CREATE DATABASE IF NOT EXISTS   Dataemp")
            cursor.execute("USE Dataemp")
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS DATA ("
                "Id VARCHAR(20) PRIMARY KEY, "
                "Name VARCHAR(50), "
                "Phone VARCHAR(20), "
                "Role VARCHAR(50), "
                "Gender VARCHAR(20), "
                "Salary DECIMAL(10,2))"
            )
        connection.close()
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong: {e}")
        return

def insert(id, name, phone, role, gender, salary):
    try:
        connection = pymysql.connect(host="localhost", user="root", password="9398", database="Dataemp")
        with connection.cursor() as cursor:
            query = "INSERT INTO DATA (Id, Name, Phone, Role, Gender, Salary) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (id, name, phone, role, gender, salary))
        connection.commit()
        connection.close()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to insert data: {e}")

def id_exists(id):
    try:
        connection = pymysql.connect(host="localhost", user="root", password="9398", database="Dataemp")
        with connection.cursor() as cursor:
            query = "SELECT COUNT(*) AS count FROM DATA WHERE Id = %s"
            cursor.execute(query, (id,))
            result = cursor.fetchone()
        connection.close()
        return result[0] > 0
    except Exception as e:
        messagebox.showerror("Error", f"Failed to check ID existence: {e}")
        return False

def fetch_employees():
    try:
        connection = pymysql.connect(host="localhost", user="root", password="9398", database="Dataemp")
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM DATA")
            result = cursor.fetchall()
        connection.close()
        return result
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch employees: {e}")
        return []

def update(id, new_name, new_phone, new_role, new_gender, new_salary):
    try:
        connection = pymysql.connect(host="localhost", user="root", password="9398", database="Dataemp")
        with connection.cursor() as cursor:
            query = "UPDATE DATA SET Name=%s, Phone=%s, Role=%s, Gender=%s, Salary=%s WHERE Id=%s"
            cursor.execute(query, (new_name, new_phone, new_role, new_gender, new_salary, id))
        connection.commit()
        connection.close()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to update data: {e}")

def delete(id):
    try:
        connection = pymysql.connect(host="localhost", user="root", password="9398", database="Dataemp")
        with connection.cursor() as cursor:
            query = "DELETE FROM DATA WHERE Id = %s"
            cursor.execute(query, (id,))
        connection.commit()
        connection.close()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to delete data: {e}")

def search(option, value):
    try:
        connection = pymysql.connect(host="localhost", user="root", password="9398", database="Dataemp")
        with connection.cursor() as cursor:
            query = f"SELECT * FROM DATA WHERE {option} = %s"
            cursor.execute(query, (value,))
            result = cursor.fetchall()
        connection.close()
        return result
    except Exception as e:
        messagebox.showerror("Error", f"Failed to search data: {e}")
        return []

def delete_all_records():
    try:
        connection = pymysql.connect(host="localhost", user="root", password="9398", database="Dataemp")
        with connection.cursor() as cursor:
            cursor.execute("TRUNCATE TABLE DATA")
        connection.commit()
        connection.close()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to delete all records: {e}")

connection_database()
