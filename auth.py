import bcrypt
import getpass
from database import create_connection
from sqlite3 import Error

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')  # Decode the byte string

def verify_password(stored_password, provided_password):
    return bcrypt.checkpw(provided_password.encode('utf-8'), stored_password.encode('utf-8'))  # Encode both as bytes

def register_user(conn, email, password):
    hashed_password = hash_password(password)
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Users (email, password_hash) VALUES (?, ?)", (email, hashed_password))
        conn.commit()
    except Error as e:
        print(f"Error registering user: {e}")

def login_user(conn):
    email = input("Enter email: ")
    password = getpass.getpass("Enter password: ")  # This line is modified

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT user_id, password_hash, user_type FROM Users WHERE email = ?", (email,))
        user_record = cursor.fetchone()

        if user_record and bcrypt.checkpw(password.encode('utf-8'), user_record[1].encode('utf-8')):
            print("Login successful!")
            return user_record[0], user_record[2]  # user_id and user_type
        else:
            print("Login failed.")
            return None, None
    except Error as e:
        print(f"Error during login: {e}")
        return None, None

