from database.models import save_question_to_db, save_answer_to_db, get_random_question_from_db
from ai.question_generator import generate_question
from ai.answer_rating import rate_answer

def main():
    print("Welcome to Interview Hell AI Testing")
    while True:
        print("\nOptions:")
        print("1. Generate Question")
        print("2. Rate Answer")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            job_offer = input("Enter job offer title: ")
            category = input("Enter category: ")
            question = generate_question(job_offer, category)
            print(f"Generated Question: {question}")
            rating = int(input("Rate the question (0-10): "))
            save_question_to_db(job_offer, category, question, rating)

        elif choice == "2":
            question, category, job_offer = get_random_question_from_db()
            print(f"Job Offer: {job_offer}, Category: {category}, Question: {question}")
            answer = input("Enter your answer: ")
            ai_rating = rate_answer(question, answer)
            print(f"AI rated your answer: {ai_rating}/10")
            feedback = int(input("Give feedback on AI rating (0-10): "))
            save_answer_to_db(question, answer, ai_rating, feedback)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
