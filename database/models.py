from database.connection import connect_db

def save_question_to_db(job_offer, category, question, rating):
    """
    Save a question to the Questions table in the database.

    Args:
        job_offer (str): The title of the job offer for which the question is intended.
        category (str): The category of the question (e.g. "HR", "Technical", or "Problem Solving").
        question (str): The text of the question.
        rating (int): The rating of the question (from 0 to 10).

    Returns:
        None
    """
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
    """
    Retrieve a random question from the database.

    This function selects a random question from the Questions table, along with its associated
    category name and job offer title. It returns a single random record containing the question
    text, category name, and job offer title.

    Returns:
        tuple: A tuple containing the question text (str), category name (str), and job offer title (str).
    """

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
    """
    Save an answer to the database.

    This function stores an answer to a question in the Answers table. The answer is associated
    with a specific question by using the question's text to look up its id in the Questions table.
    The function also stores the AI's rating of the answer, as well as user feedback on the AI's
    rating.

    Args:
        question (str): The text of the question.
        answer (str): The text of the answer.
        ai_rating (int): The AI's rating of the answer (0-10).
        feedback (int): User feedback on the AI's rating (0-10).

    Returns:
        None
    """
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


def get_all_offers_and_questions():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT j.title, q.text FROM JobOffers j
        INNER JOIN Questions q
        ON j.id = q.job_offer_id
        """
    )
    result = cursor.fetchall()
    conn.close()
    return result


