# from fastapi import FastAPI
# from transformers import pipeline
# from pydantic import BaseModel
#
#
# class Item(BaseModel):
#     text: str
#
#
# app = FastAPI()
# classifier = pipeline("text-classification", model="cointegrated/rubert-tiny2-cedr-emotion-detection")
#
#
# @app.get("/")
# def root():
#     return {"message": "We'd like to welcome"}
#
#
# @app.post("/predict/")
# def predict(item: Item):
#     """Analyzing the emotion of the text"""
#
#     return classifier(item.text)[0]

from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel


class Item(BaseModel):
    text: str


app = FastAPI()
classifier = pipeline("sentiment-analysis")


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/predict/")
def predict(item: Item):
    return classifier(item.text)[0]