import streamlit as st
import pandas as pd

st.header("Mark's Very Good and Official Performance Information")

# inputs
show_date = st.date_input("What's today's date?")
show_name = st.selectbox("Pick one", ["DogProv", "Portal-prov", "Fire & Beer"])
show_estimate = st.slider("How did you think the show would go?", 0, 10)
show_actual = st.slider("How did the show actually go?", 0, 10)
new_record = [show_date, show_name, show_estimate, show_actual]

# Snowflake connection
# doesn't work, st.connect or st.connection
# conn = st.connect(**st.secrets["snowflake"])

# initialize dataframe
df = pd.DataFrame(new_record, columns=["raw_input"])

st.dataframe(df)
