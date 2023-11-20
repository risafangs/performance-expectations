import streamlit as st
import pandas as pd

st.header("Mark's Very Good and Official Performance Information")

# inputs
show_date = st.date_input("What's today's date?")
show_name = st.selectbox("Pick one", ["DogProv", "Portal-prov", "Fire & Beer"])
score_estimate = st.slider("How did you think the show would go?", 0, 10)
score_actual = st.slider("How did the show actually go?", 0, 10)
new_input = dict(show_date, show_name, score_estimate, score_actual)

# Snowflake connection
# doesn't work, st.connect or st.connection
# conn = st.connect(**st.secrets["snowflake"])

# initialize dataframe
df = pd.DataFrame(new_input)

st.dataframe(df)
