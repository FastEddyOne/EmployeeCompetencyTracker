def add_competency(conn, name):
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Competencies (name, date_created) VALUES (?, datetime('now'))", (name,))
        conn.commit()
        print("Competency added successfully.")
    except Error as e:
        print(f"Error adding competency: {e}")

def view_competencies(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT competency_id, name FROM Competencies")
        competencies = cursor.fetchall()

        if competencies:
            for comp in competencies:
                print(f"{comp[0]}: {comp[1]}")
        else:
            print("No competencies found.")
    except Error as e:
        print(f"Error retrieving competencies: {e}")

def edit_competency(conn, competency_id, name):
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE Competencies SET name = ? WHERE competency_id = ?", (name, competency_id))
        conn.commit()
        print("Competency updated successfully.")
    except Error as e:
        print(f"Error updating competency: {e}")

def delete_competency(conn, competency_id):
    try:
        confirm = input(f"Are you sure you want to delete competency with ID {competency_id}? (yes/no): ")
        if confirm.lower() != 'yes':
            print("Competency deletion canceled.")
            return

        cursor = conn.cursor()
        cursor.execute("DELETE FROM Competencies WHERE competency_id = ?", (competency_id,))
        conn.commit()
        print("Competency deleted successfully.")
    except Error as e:
        print(f"Error deleting competency: {e}")

def view_my_competencies(conn, user_id):
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT c.name, ar.score, ar.date_taken
            FROM Competencies c
            JOIN Assessments a ON c.competency_id = a.competency_id
            JOIN Assessment_Results ar ON a.assessment_id = ar.assessment_id
            WHERE ar.user_id = ?
        """, (user_id,))
        results = cursor.fetchall()

        if results:
            print(f"\nCompetency Summary for User ID {user_id}:")
            for result in results:
                print(f"Competency: {result[0]}, Score: {result[1]}, Date: {result[2]}")
        else:
            print("No competencies found for this user.")
    except Error as e:
        print(f"Error fetching competencies: {e}")
