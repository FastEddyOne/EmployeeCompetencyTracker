from sqlite3 import Error
from auth import hash_password

def view_users(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT user_id, first_name, last_name, email, user_type FROM Users")
        users = cursor.fetchall()
        
        if users:
            for user in users:
                print(f"{user[0]}: {user[1]} {user[2]}, {user[3]}, {user[4]}")
        else:
            print("No users found.")
            
    except Error as e:
        print(f"Error retrieving users: {e}")

def add_user(conn, first_name, last_name, email, password, user_type):
    hashed_password = hash_password(password)
    try:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Users (first_name, last_name, email, password_hash, user_type, date_created)
            VALUES (?, ?, ?, ?, ?, datetime('now'))
        """, (first_name, last_name, email, hashed_password, user_type))
        conn.commit()
    except Error as e:
        print(f"Error adding user: {e}")

def edit_user(conn, user_id, first_name, last_name, email, phone, user_type):
    try:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE Users
            SET first_name = ?, last_name = ?, email = ?, phone = ?, user_type = ?
            WHERE user_id = ?
        """, (first_name, last_name, email, phone, user_type, user_id))
        conn.commit()
    except Error as e:
        print(f"Error updating user: {e}")

def delete_user(conn, user_id):
    try:
        confirm = input(f"Are you sure you want to delete user with ID {user_id}? (yes/no): ")
        if confirm.lower() != 'yes':
            print("User deletion canceled.")
            return

        cursor = conn.cursor()
        cursor.execute("DELETE FROM Users WHERE user_id = ?", (user_id,))
        conn.commit()
        print("User deleted successfully.")
    except Error as e:
        print(f"Error deleting user: {e}")
