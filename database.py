import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        print("SQLite DB connected")
        return conn
    except Error as e:
        print(e)

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        conn.commit()
        print("Table created successfully.")
    except Error as e:
        print(f"Error occurred while creating table: {e}")

def initialize_database():
    database = "competency_tracker.db"

    sql_create_users_table = """ CREATE TABLE IF NOT EXISTS Users (
                                    user_id INTEGER PRIMARY KEY,
                                    first_name TEXT NOT NULL,
                                    last_name TEXT NOT NULL,
                                    phone TEXT,
                                    email TEXT NOT NULL UNIQUE,
                                    password_hash TEXT NOT NULL,
                                    active_status BOOLEAN NOT NULL DEFAULT 1,
                                    date_created DATE NOT NULL,
                                    hire_date DATE,
                                    user_type TEXT NOT NULL CHECK(user_type IN ('user', 'manager'))
                                ); """

    sql_create_competencies_table = """ CREATE TABLE IF NOT EXISTS Competencies (
                                            competency_id INTEGER PRIMARY KEY,
                                            name TEXT NOT NULL,
                                            date_created DATE NOT NULL
                                        ); """

    sql_create_assessments_table = """ CREATE TABLE IF NOT EXISTS Assessments (
                                           assessment_id INTEGER PRIMARY KEY,
                                           name TEXT NOT NULL,
                                           date_created DATE NOT NULL,
                                           competency_id INTEGER NOT NULL,
                                           FOREIGN KEY (competency_id) REFERENCES Competencies (competency_id)
                                       ); """

    sql_create_assessment_results_table = """ CREATE TABLE IF NOT EXISTS Assessment_Results (
                                                 result_id INTEGER PRIMARY KEY,
                                                 user_id INTEGER NOT NULL,
                                                 assessment_id INTEGER NOT NULL,
                                                 score INTEGER CHECK(score BETWEEN 0 AND 4),
                                                 date_taken DATE NOT NULL,
                                                 manager_id INTEGER,
                                                 FOREIGN KEY (user_id) REFERENCES Users (user_id),
                                                 FOREIGN KEY (assessment_id) REFERENCES Assessments (assessment_id),
                                                 FOREIGN KEY (manager_id) REFERENCES Users (user_id)
                                             ); """

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn:
        create_table(conn, sql_create_users_table)
        create_table(conn, sql_create_competencies_table)
        create_table(conn, sql_create_assessments_table)
        create_table(conn, sql_create_assessment_results_table)

        conn.close()
    else:
        print("Error! Cannot create the database connection.")

if __name__ == '__main__':
    initialize_database()
