import streamlit as st
import pandas as pd
import snowflake.connector

st.header("Mark's Very Good and Official Performance Information")

# inputs
show_date = st.date_input("What's today's date?")
show_name = st.selectbox("Pick one", ["DogProv", "Portal-prov", "Fire & Beer"])
show_estimate = st.slider("How did you think the show would go?", 0, 10)
show_actual = st.slider("How did the show actually go?", 0, 10)

# Snowflake connection
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])

# add inputs to Snowflake
# new_inputs = insert_row_snowflake(show_date, show_name, show_estimate, show_actual)
# streamlit.text(new_inputs)
