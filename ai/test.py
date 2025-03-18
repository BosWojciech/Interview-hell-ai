# Use a pipeline as a high-level helper
from transformers import pipeline
import torch

if torch.cuda.is_available():
    device = 0  # Use the first GPU
    print(f"Using GPU: {torch.cuda.get_device_name(device)}")
else:
    device = -1 # Use CPU
    print("Using CPU")

prompt = """
Imagine there is a company Hell Inc. that searches for an employee.
You are an AI that helps the company to create interview question.
You are given a job title and a category of a question and your job is to generate a question.
Your response should be only one question that is humoristic and relevant to the job title and the category.
Job Title: Torture Tester
Question Category: Technical Questions"
"""

# pipe = pipeline("text-generation", model="openai-community/gpt2-xl")
# https://huggingface.co/HuggingFaceH4/zephyr-7b-beta
# https://huggingface.co/tiiuae/falcon-7b
# pipe = pipeline("text-generation", model="bigscience/bloom") 320GB


pipe = pipeline("text-generation", model="deepseek-ai/DeepSeek-R1-Distill-Qwen-7B")

def generate_question(prompt):
    messages = [
        {"role": "user", "content": prompt},
    ]
    return pipe(messages)[0]['generated_text']

print(generate_question(prompt))
