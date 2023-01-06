import torch


from transformers import pipeline

classifier = pipeline("sentiment-analysis")

res = classifier("These are not the droids you've been looking for")

print(res)
