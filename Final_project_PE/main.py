import streamlit as st
from transformers import pipeline


pipe = pipeline("summarization", model="IlyaGusev/rut5_base_sum_gazeta")

st.title('Суммаризация текста')
st.subheader("Данное приложение поможет пользователю преобразовать текст в конкретные тезисы")
text = st.text_input('Введите текст', 'пример: Я люблю программную инженерию')
result = st.button('Сократить текст')

if result:
    st.markdown("Работаем....")
    st.markdown("...еще немного")
    st.write('**Результаты:**')
    st.write(pipe(text))