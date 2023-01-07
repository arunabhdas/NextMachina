import torch

from transformers import pipeline

classifier = pipeline("sentiment-analysis")

res = classifier("The way to achieve consciousness is through quantum gravity research")

print(res)
