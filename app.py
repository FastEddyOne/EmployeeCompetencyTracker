import csv
import os
import bcrypt
from datetime import datetime
from sqlite3 import Error
from database import create_connection, initialize_database
from user_management import view_users, add_user, edit_user, delete_user
from competency_management import add_competency, view_competencies, edit_competency, delete_competency, view_my_competencies
from assessment_management import add_assessment, view_assessments, edit_assessment, delete_assessment
from assessment_results_management import add_assessment_result, view_assessment_results, edit_assessment_result, delete_assessment_result
from report_generation import generate_user_competency_summary, generate_competency_results_summary
from csv_operations import import_assessment_results_from_csv, import_data_from_csv, export_data_to_csv
from pdf_operations import generate_pdf_report

def login_user(conn):
    email = input("Enter email: ")
    password = input("Enter password: ")

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

def user_management_menu(conn):
    while True:
        print("\nUser Management Menu")
        print("1. View Users")
        print("2. Add User")
        print("3. Edit User")
        print("4. Delete User")
        print("5. Return to Main Menu")

        choice = input("Enter choice: ")

        if choice == '1':
            view_users(conn)
        elif choice == '2':
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            email = input("Enter email: ")
            password = input("Enter password: ")
            user_type = input("Enter user type ('user' or 'manager'): ")
            add_user(conn, first_name, last_name, email, password, user_type)
        elif choice == '3':
            user_id = input("Enter user ID to edit: ")
            first_name = input("Enter new first name: ")
            last_name = input("Enter new last name: ")
            email = input("Enter new email: ")
            phone = input("Enter new phone: ")
            user_type = input("Enter new user type ('user' or 'manager'): ")
            edit_user(conn, user_id, first_name, last_name, email, phone, user_type)
        elif choice == '4':
            user_id = input("Enter user ID to delete: ")
            delete_user(conn, user_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again.")

def competency_management_menu(conn):
    while True:
        print("\nCompetency Management Menu")
        print("1. View Competencies")
        print("2. Add Competency")
        print("3. Edit Competency")
        print("4. Delete Competency")
        print("5. Return to Main Menu")

        choice = input("Enter choice: ")

        if choice == '1':
            view_competencies(conn)
        elif choice == '2':
            name = input("Enter competency name: ")
            add_competency(conn, name)
        elif choice == '3':
            competency_id = input("Enter competency ID to edit: ")
            name = input("Enter new competency name: ")
            edit_competency(conn, competency_id, name)
        elif choice == '4':
            competency_id = input("Enter competency ID to delete: ")
            delete_competency(conn, competency_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again.")

def assessment_management_menu(conn):
    while True:
        print("\nAssessment Management Menu")
        print("1. View Assessments")
        print("2. Add Assessment")
        print("3. Edit Assessment")
        print("4. Delete Assessment")
        print("5. Add Assessment Result")
        print("6. View Assessment Results")
        print("7. Edit Assessment Result")
        print("8. Delete Assessment Result")
        print("9. Return to Main Menu")

        choice = input("Enter choice: ")

        if choice == '1':
            view_assessments(conn)
        elif choice == '2':
            name = input("Enter assessment name: ")
            competency_id = input("Enter competency ID: ")
            add_assessment(conn, name, competency_id)
        elif choice == '3':
            assessment_id = input("Enter assessment ID to edit: ")
            name = input("Enter new assessment name: ")
            competency_id = input("Enter new competency ID: ")
            edit_assessment(conn, assessment_id, name, competency_id)
        elif choice == '4':
            assessment_id = input("Enter assessment ID to delete: ")
            delete_assessment(conn, assessment_id)
        elif choice == '5':
            user_id = input("Enter user ID: ")
            assessment_id = input("Enter assessment ID: ")
            score = input("Enter score (0-4): ")
            date_taken = input("Enter date taken (YYYY-MM-DD): ")
            manager_id = input("Enter manager ID: ")
            add_assessment_result(conn, user_id, assessment_id, score, date_taken, manager_id)
        elif choice == '6':
            view_assessment_results(conn)
        elif choice == '7':
            result_id = input("Enter the assessment result ID to edit: ")
            # logic for fetching and editing the assessment result
        elif choice == '8':
            result_id = input("Enter assessment result ID to delete: ")
            delete_assessment_result(conn, result_id)
        elif choice == '9':
            break
        else:
            print("Invalid choice, please try again.")


def report_generation_menu(conn):
    while True:
        print("\nReport Generation Menu")
        print("1. Generate User Competency Summary")
        print("2. Generate Competency Results Summary")
        print("3. Generate PDF User Competency Summary")
        print("4. Return to Main Menu")

        choice = input("Enter choice: ")

        if choice == '1':
            user_id = input("Enter user ID for the summary: ")
            summary_data = generate_user_competency_summary(conn, user_id)
            if summary_data:
                for line in summary_data:
                    print(line)
            else:
                print(f"No competency data found for user ID {user_id}.")
        elif choice == '2':
            competency_id = input("Enter competency ID for the summary: ")
            generate_competency_results_summary(conn, competency_id)
        elif choice == '3':
            user_id = input("Enter user ID for the PDF summary: ")
            data = generate_user_competency_summary(conn, user_id)
            file_name = f"reports/user_competency_summary_{user_id}.pdf"
            generate_pdf_report(file_name, data)
            print(f"PDF report generated: {file_name}")
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")

def csv_operations_menu(conn):
    while True:
        print("\nCSV Operations Menu")
        print("1. Import Data from CSV")
        print("2. Export Data to CSV")
        print("3. Import Assessment Results from CSV")
        print("4. Return to Main Menu")

        choice = input("Enter choice: ")

        if choice == '1':
            table_name = input("Enter the table name to import data into: ")
            file_path = input("Enter the path of the CSV file to import: ")
            import_data_from_csv(conn, table_name, file_path)
        elif choice == '2':
            table_name = input("Enter the table name to export: ")
            file_name = input("Enter the file name for the CSV export: ")
            export_data_to_csv(conn, table_name, file_name)
        elif choice == '3':
            file_path = input("Enter the path of the CSV file to import assessment results: ")
            import_assessment_results_from_csv(conn, file_path)
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")

def register_user(conn):
    print("\nUser Registration")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    phone = input("Enter phone number (optional): ")
    hire_date = input("Enter hire date (YYYY-MM-DD, optional): ")
    user_type = input("Enter user type ('user' or 'manager'): ")
    date_created = datetime.now().strftime('%Y-%m-%d')  # Format date as YYYY-MM-DD

    try:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Users 
            (first_name, last_name, phone, email, password_hash, active_status, date_created, hire_date, user_type) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (first_name, last_name, phone, email, hashed_password, 1, date_created, hire_date or None, user_type))
        conn.commit()
        print("User registered successfully.")
    except Error as e:
        print(f"Error registering user: {e}")

def main_menu():
    conn = create_connection("competency_tracker.db")
    initialize_database()

    while True:
        print("\nMain Menu")
        print("1. Login")
        print("2. Register")
        print("X. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            user_id, user_type = login_user(conn)
            if user_id is None:
                print("Login failed or cancelled. Try again.")
            else:
                user_specific_menu(conn, user_id, user_type)
        elif choice == '2':
            register_user(conn)
        elif choice.upper() == 'X':
            print("Exiting application.")
            break
        else:
            print("Invalid choice, please try again.")

    conn.close()
    print("Application exited successfully.")

def user_specific_menu(conn, user_id, user_type):
    if user_type == 'manager':
        # Manager-specific options
        while True:
            print("\nManager Menu")
            print("1. User Management")
            print("2. Competency Management")
            print("3. Assessment Management")
            print("4. Report Generation")
            print("5. CSV Operations")
            print("X. Logout")

            choice = input("Enter choice: ")

            if choice == '1':
                user_management_menu(conn)
            elif choice == '2':
                competency_management_menu(conn)
            elif choice == '3':
                assessment_management_menu(conn)
            elif choice == '4':
                report_generation_menu(conn)
            elif choice == '5':
                csv_operations_menu(conn)
            elif choice.upper() == 'X':
                break
            else:
                print("Invalid choice, please try again.")
    else:
        # User-specific options
        while True:
            print("\nUser Menu")
            print("1. View My Competencies")
            print("X. Logout")

            choice = input("Enter choice: ")

            if choice == '1':
                view_my_competencies(conn, user_id)
            elif choice.upper() == 'X':
                break
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    main_menu()