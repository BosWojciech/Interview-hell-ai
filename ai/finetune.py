import psycopg2
from transformers import GPT2Tokenizer
from datasets import Dataset
from transformers import GPT2LMHeadModel
from transformers import Trainer, DataCollatorForLanguageModeling
from transformers import TrainingArguments

conn = psycopg2.connect(
    "dbname=interviewhell",
    user="postgres",
    password="zaq12WSX",
    host="localhost",
    port="5432"
    )

cursor = conn.cursor()
cursor.execute("select joboffers.title, categories.name, questions.text from questions, joboffers, categories;")

result = cursor.fetchall()
print(result)
conn.close()

train_data = []
formatted_data_boilerplate = """
Job Title: {}
Question Category: {}
Interview Question: {}
"""
for row in result:
    train_data.append(formatted_data_boilerplate.format(row[0], row[1], row[2]))

print(train_data)

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
tokenizer.pad_token = tokenizer.eos_token

# Tokenize the list of prompts
def tokenize_function(examples):
    return tokenizer(examples["text"], truncation=True, padding="max_length", max_length=200)

# Convert list to Hugging Face dataset format
dataset = Dataset.from_dict({"text": train_data}).map(tokenize_function, batched=True)

# Load GPT-2 model
model = GPT2LMHeadModel.from_pretrained("gpt2")

# Assign the padding token to avoid errors
model.config.pad_token_id = tokenizer.pad_token_id

training_args = TrainingArguments(
    output_dir="./gpt2-job-interviews",
    overwrite_output_dir=True,
    num_train_epochs=3,        # You can increase this if needed
    per_device_train_batch_size=2,  # Adjust batch size based on your GPU/CPU
    save_steps=500,
    save_total_limit=2,
    logging_dir="./logs",
    logging_steps=50
)

# Create a data collator (ensures padding is handled correctly)
data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer,
    mlm=False  # We are training GPT-2, not using masked language modeling (MLM)
)

# Initialize Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
    data_collator=data_collator
)

trainer.train()

model.save_pretrained("./gpt2-job-interview-finetuned")
tokenizer.save_pretrained("./gpt2-job-interview-finetuned")