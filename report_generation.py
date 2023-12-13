def generate_user_competency_summary(conn, user_id):
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT c.name, MAX(ar.score), MAX(ar.date_taken)
            FROM Competencies c
            JOIN Assessments a ON c.competency_id = a.competency_id
            JOIN Assessment_Results ar ON a.assessment_id = ar.assessment_id
            WHERE ar.user_id = ?
            GROUP BY c.competency_id
        """, (user_id,))
        results = cursor.fetchall()

        summary_data = [f"Competency: {result[0]}, Score: {result[1]}, Date: {result[2]}" for result in results]
        return summary_data
    except Error as e:
        print(f"Error generating user competency summary: {e}")
        return []

def generate_competency_results_summary(conn, competency_id):
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT u.user_id, u.first_name, u.last_name, MAX(ar.score), MAX(a.name), MAX(ar.date_taken)
            FROM Users u
            JOIN Assessment_Results ar ON u.user_id = ar.user_id
            JOIN Assessments a ON ar.assessment_id = a.assessment_id
            WHERE a.competency_id = ?
            GROUP BY u.user_id
        """, (competency_id,))
        results = cursor.fetchall()

        print(f"\nResults Summary for Competency ID {competency_id}:")
        for result in results:
            print(f"User: {result[0]} - {result[1]} {result[2]}, Score: {result[3]}, Assessment: {result[4]}, Date: {result[5]}")
    except Error as e:
        print(f"Error generating competency results summary: {e}")

def fetch_user_competency_summary_for_pdf(conn, user_id):
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT c.name, MAX(ar.score), MAX(ar.date_taken)
            FROM Competencies c
            JOIN Assessments a ON c.competency_id = a.competency_id
            JOIN Assessment_Results ar ON a.assessment_id = ar.assessment_id
            WHERE ar.user_id = ?
            GROUP BY c.competency_id
        """, (user_id,))
        results = cursor.fetchall()

        return [f"Competency: {result[0]}, Score: {result[1]}, Date: {result[2]}" for result in results]
    except Error as e:
        print(f"Error fetching data for PDF summary: {e}")
        return []
