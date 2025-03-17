# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text-generation", model="openai-community/gpt2")

prompt = """
Job Title: Satan's Feet Tickler

Job Description: You will be responsible for providing foot relaxation services to infernal beings, ensuring optimal tickling effectiveness while maintaining professionalism in high-temperature environments.

Interview Questions:
1.Why do you think you are the best fit for scratching Satan's butt?
2.What motivates you to work in such a personal role?
3.How do you handle situations where Satan might be unhappy with your work?
4.What tools or techniques would you use for optimal butt-scratching?
5.Describe your past experience with similar tasks.
6.How would you innovate in the field of infernal hygiene?
7.What would you do if Satan's tail got in the way?
8.How would you handle a situation where lava spilled during your task?
9.If your scratching tool breaks, how do you improvise?
10."""


# Generate a question
question = pipe(prompt, max_length=1000, num_return_sequences=1)
print(question[0]["generated_text"])

