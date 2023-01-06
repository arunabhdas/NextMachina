import torch

from transformers import pipeline

generator = pipeline("text-generation", model="distilgpt2")

res = generator(
    "I am the famous author Lewis Carrol. And my new book is ",
    max_length=300,
    num_return_sequences=2,
)

print(res)
