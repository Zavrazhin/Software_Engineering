import streamlit as st
import requests


st.title('Суммаризация текста')
st.subheader("Данное приложение поможет пользователю преобразовать текст в конкретные тезисы")
text = st.text_input('Введите текст', 'пример: Я люблю распределенные вычисления')
result = st.button('Сократить текст')

if result:
    response = requests.post('http://127.0.0.1:8000/predict',
                             json={'text': text})
    st.markdown("Работаем....")
    st.markdown("...еще немного")
    st.write('**Результаты:**')
    st.write(response.json())
