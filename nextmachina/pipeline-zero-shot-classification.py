import torch

from transformers import pipeline

classifier = pipeline("zero-shot-classification")

res = classifier(
    "We are the droids that we've been looking for all along",
    candidate_labels=["science fiction", "documentary", "economics", "politics", "social science"]
)

print(res)
