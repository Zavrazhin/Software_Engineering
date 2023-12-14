from transformers import pipeline

pipe = pipeline("text-classification", "SamLowe/roberta-base-go_emotions")
pipe("I love machine learning engineering")
