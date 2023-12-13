import csv
import os
from sqlite3 import Error
from assessment_results_management import add_assessment_result  # Import the required function

def import_data_from_csv(conn, table_name, file_path):
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            columns = ','.join(reader.fieldnames)
            placeholders = ','.join(['?'] * len(reader.fieldnames))

            cursor = conn.cursor()
            for row in reader:
                values = tuple(row[field] for field in reader.fieldnames)
                cursor.execute(f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})", values)

            conn.commit()
            print(f"Data imported successfully from {file_path} to {table_name}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Error as e:
        print(f"Error importing data: {e}")

def import_assessment_results_from_csv(conn, file_path):
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                add_assessment_result(
                    conn, 
                    row['user_id'], 
                    row['assessment_id'], 
                    row['score'], 
                    row['date_taken'], 
                    row['manager_id']
                )
    except Error as e:
        print(f"Error importing data: {e}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def export_data_to_csv(conn, table_name, file_name):
    reports_folder = 'reports'
    if not os.path.exists(reports_folder):
        os.makedirs(reports_folder)

    file_path = os.path.join(reports_folder, file_name)
    query = f"SELECT * FROM {table_name}"

    try:
        cursor = conn.cursor()
        cursor.execute(query)
        data = cursor.fetchall()

        headers = [description[0] for description in cursor.description]

        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerows(data)

        print(f"Data exported successfully to {file_path}")
    except Error as e:
        print(f"Error exporting data from {table_name}: {e}")

