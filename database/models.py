from database.connection import connect_db

def save_question_to_db(job_offer, category, question, rating):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO Questions (job_offer_id, category_id, text, rating)
        VALUES ((SELECT id FROM JobOffers WHERE title = %s),
                (SELECT id FROM Categories WHERE name = %s),
                %s, %s)
        """,
        (job_offer, category, question, rating)
    )
    conn.commit()
    conn.close()

def get_random_question_from_db():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT q.text, c.name, j.title
        FROM Questions q
        JOIN Categories c ON q.category_id = c.id
        JOIN JobOffers j ON q.job_offer_id = j.id
        ORDER BY RANDOM()
        LIMIT 1
        """
    )
    result = cursor.fetchone()
    conn.close()
    return result

def save_answer_to_db(question, answer, ai_rating, feedback):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO Answers (question_id, text, ai_rating, user_feedback)
        VALUES ((SELECT id FROM Questions WHERE text = %s), %s, %s, %s)
        """,
        (question, answer, ai_rating, feedback)
    )
    conn.commit()
    conn.close()
