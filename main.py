import streamlit as st
import pandas as pd
#from snowflake.snowpark import Session
from streamlit_gsheets import GSheetsConnection

st.header("Mark's Very Good and Official Performance Information")

# inputs
date = st.date_input("What's today's date?")
show_name = st.selectbox("Pick one", ["DogProv", "Portal-prov", "Fire & Beer"])
score_estimate = st.slider("How did you think the show would go?", 0, 10)
score_actual = st.slider("How did the show actually go?", 0, 10)
# new_input = dict(show_date, show_name, score_estimate, score_actual)

# Establish Snowflake session
# this doesn't work - the SSO redirect fails
#@st.cache_resource
#def create_session():
#    return Session.builder.configs(st.secrets.snowflake).create()

#session = create_session()
#st.success("Connected to Snowflake!")

# Connect to google sheets
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read()

# Print Sheet results
#for row in df.itertuples():
#    st.write(f"The {row.show_name} show on {row.date} had an estimated score of {row.score_estimate} but was actually a {row.score_actual}") 
