import torch

from transformers import pipeline

classifier = pipeline("sentiment-analysis")

res = classifier("I'm so happy that spring is going to be here soon")

print(res)
