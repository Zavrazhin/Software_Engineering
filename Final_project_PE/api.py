from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline


class Item(BaseModel):
    text: str


app = FastAPI()
pipe = pipeline("summarization", model="IlyaGusev/rut5_base_sum_gazeta")


@app.get("/")
def root():
    return {"msg": "welcome to our API, we'll help you shorten the text"}


@app.post("/predict/")
def predict(item: Item):
    """Summarization text"""

    return pipe(item.text)
