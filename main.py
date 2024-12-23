from database.models import get_all_offers_and_questions
from ai.question_generator import QuestionGenerator


data = get_all_offers_and_questions()
question_generator = QuestionGenerator()

print("Training the model...")
question_generator.train(data)

print("Generating questions...")
job_title = "Ginger People Torture Specialist"
questions = question_generator.generate_question(job_title, num_return_sequences=3)

print("Generated Questions:")
for i, q in enumerate(questions, 1):
    print(f"{i}. {q}")





