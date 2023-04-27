import streamlit as st
import pandas as pd
import preprocessor,helper

df = preprocessor.preprocess()

user_menu = st.sidebar.radio(
    'select an Option',
    ('Medal Tally','Overall Analysis','Country-wise Analysis','Athlete wise Analysis')
)
 
st.dataframe(df)

if user_


 