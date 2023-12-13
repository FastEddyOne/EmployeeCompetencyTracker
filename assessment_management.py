def add_assessment(conn, name, competency_id):
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Assessments (name, date_created, competency_id) VALUES (?, datetime('now'), ?)", (name, competency_id))
        conn.commit()
        print("Assessment added successfully.")
    except Error as e:
        print(f"Error adding assessment: {e}")


def view_assessments(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT assessment_id, name, competency_id FROM Assessments")
        assessments = cursor.fetchall()

        if assessments:
            for assessment in assessments:
                print(f"{assessment[0]}: {assessment[1]}, Competency ID: {assessment[2]}")
        else:
            print("No assessments found.")
    except Error as e:
        print(f"Error retrieving assessments: {e}")

def edit_assessment(conn, assessment_id, name, competency_id):
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE Assessments SET name = ?, competency_id = ? WHERE assessment_id = ?", (name, competency_id, assessment_id))
        conn.commit()
        print("Assessment updated successfully.")
    except Error as e:
        print(f"Error updating assessment: {e}")

def delete_assessment(conn, assessment_id):
    try:
        confirm = input(f"Are you sure you want to delete assessment with ID {assessment_id}? (yes/no): ")
        if confirm.lower() != 'yes':
            print("Assessment deletion canceled.")
            return

        cursor = conn.cursor()
        cursor.execute("DELETE FROM Assessments WHERE assessment_id = ?", (assessment_id,))
        conn.commit()
        print("Assessment deleted successfully.")
    except Error as e:
        print(f"Error deleting assessment: {e}")

def get_assessment_result_by_id(conn, result_id):
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT user_id, assessment_id, score, date_taken, manager_id
            FROM Assessment_Results
            WHERE result_id = ?
        """, (result_id,))
        result = cursor.fetchone()
        if result:
            return {
                'user_id': result[0],
                'assessment_id': result[1],
                'score': result[2],
                'date_taken': result[3],
                'manager_id': result[4]
            }
        return None
    except Error as e:
        print(f"Error retrieving assessment result: {e}")
        return None
