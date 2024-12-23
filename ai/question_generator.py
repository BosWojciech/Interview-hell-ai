import torch
from torch.utils.data import Dataset, DataLoader
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, AdamW
import nltk
from nltk.tokenize import word_tokenize
import random
import os

nltk.download('punkt')

class JobQuestionDataset(Dataset):
    def __init__(self, data, tokenizer, max_len=250):
        self.data = data
        self.tokenizer = tokenizer
        self.max_len = max_len
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, index):
       job_title, question = self.data[index]

       inputs = self.tokenizer(job_title, max_length=self.max_len, padding="max_length", truncation=True, return_tensors="pt")
       labels = self.tokenizer(question, max_length=self.max_len, padding="max_length", truncation=True, return_tensors="pt")

       return {
            "input_ids": inputs["input_ids"].squeeze(0),
            "attention_mask": inputs["attention_mask"].squeeze(0),
            "labels": labels["input_ids"].squeeze(0),
        }
    
class QuestionGenerator:
    def __init__(self):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = AutoTokenizer.from_pretrained("t5-large")
        self.model = AutoModelForSeq2SeqLM.from_pretrained("t5-large")
        self.max_len = 250

    def train(
            self, data, batch_size=4, epochs=5, learning_rate=2e-5, output_dir="./model"
    ):
        dataset = JobQuestionDataset(data, self.tokenizer, self.max_len)
        dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)
        
        self.model.to(self.device)
        optimizer = AdamW(self.model.parameters(), lr=learning_rate)
        self.model.train()

        for epoch in range(epochs):
            total_loss = 0
            for batch in dataloader:
                input_ids = batch["input_ids"].to(self.device)
                attention_mask = batch["attention_mask"].to(self.device)
                labels = batch["labels"].to(self.device)

                outputs = self.model(input_ids=input_ids, attention_mask=attention_mask, labels=labels)
                loss = outputs.loss
                total_loss += loss.item()

                optimizer.zero_grad()
                loss.backward()
                optimizer.step()
            print(f"Epoch {epoch + 1}/{epochs}, Loss: {total_loss / len(dataloader)}")

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        self.model.save_pretrained(output_dir)
        self.tokenizer.save_pretrained(output_dir)

    def generate_question(self, job_title, num_return_sequences=1):
        input_ids = self.tokenizer.encode(
            job_title, return_tensors="pt", max_length=self.max_len, truncation=True
        )
        input_ids = input_ids.to(self.model.device)

        outputs = self.model.generate(
            input_ids=input_ids,
            max_length=self.max_len,
            num_return_sequences=num_return_sequences,
            temperature=0.7,
            top_k=50,
            top_p=0.95,
            do_sample=True,
        )

        return [self.tokenizer.decode(output, skip_special_tokens=True) for output in outputs]
