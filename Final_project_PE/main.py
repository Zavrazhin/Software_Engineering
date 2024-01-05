import fastapi
import streamlit as st
import requests
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

    return pipe(item.text)[0]


st.title('Суммаризация текста')
st.subheader("Данное приложение поможет пользователю преобразовать текст в конкретные тезисы")
text = st.text_input('Введите текст', 'пример: Я люблю программную инженерию')
result = st.button('Сократить текст')

if result:
    response = requests.post('http://127.0.0.1:8000/predict',
                             json={'text': text})
    st.markdown("Работаем....")
    st.markdown("...еще немного")
    st.write('**Результаты:**')
    st.write(response.json())
