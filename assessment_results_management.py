def add_assessment_result(conn, user_id, assessment_id, score, date_taken, manager_id):
    try:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Assessment_Results (user_id, assessment_id, score, date_taken, manager_id)
            VALUES (?, ?, ?, ?, ?)
        """, (user_id, assessment_id, score, date_taken, manager_id))
        conn.commit()
        print("Assessment result added successfully.")
    except Error as e:
        print(f"Error adding assessment result: {e}")



def view_assessment_results(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT result_id, user_id, assessment_id, score, date_taken, manager_id
            FROM Assessment_Results
        """)
        results = cursor.fetchall()

        if results:
            for result in results:
                print(f"Result ID: {result[0]}, User ID: {result[1]}, Assessment ID: {result[2]}, Score: {result[3]}, Date Taken: {result[4]}, Manager ID: {result[5]}")
        else:
            print("No assessment results found.")
    except Error as e:
        print(f"Error retrieving assessment results: {e}")


def edit_assessment_result(conn, result_id, user_id, assessment_id, score, date_taken, manager_id):
    try:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE Assessment_Results
            SET user_id = ?, assessment_id = ?, score = ?, date_taken = ?, manager_id = ?
            WHERE result_id = ?
        """, (user_id, assessment_id, score, date_taken, manager_id, result_id))
        conn.commit()
        print("Assessment result updated successfully.")
    except Error as e:
        print(f"Error updating assessment result: {e}")


def delete_assessment_result(conn, result_id):
    try:
        confirm = input(f"Are you sure you want to delete assessment result with ID {result_id}? (yes/no): ")
        if confirm.lower() != 'yes':
            print("Assessment result deletion canceled.")
            return

        cursor = conn.cursor()
        cursor.execute("DELETE FROM Assessment_Results WHERE result_id = ?", (result_id,))
        conn.commit()
        print("Assessment result deleted successfully.")
    except Error as e:
        print(f"Error deleting assessment result: {e}")

