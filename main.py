import streamlit as st

st.header('Mark\'s Official and Very Good Performance Data')

show_date = st.date_input("What's today's date?")
show_name = st.selectbox("Pick one", ["DogProv", "Portal-prov", "Fire & Beer"])
show_estimate = st.slider("How did you think the show would go?", 0, 10)
show_actual = st.slider("How did the show actually go?", 0, 10)
