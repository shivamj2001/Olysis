import streamlit as st
import pandas as pd
import preprocessor,helper

df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')

df = preprocessor.preprocess(df,region_df)

st.sidebar.title("Olympic Analysis")

user_menu = st.sidebar.radio(
    'select an Option',
    ('Medal Tally','Overall Analysis','Country-wise Analysis','Athlete wise Analysis')
)
 


if user_menu == 'Medal Tally':
    st.sidebar.header("Medal Tally")
    years,country = helper.country_year_list(df)

    selected_year = st.sidebar.selectbox("Select Year",years)
    selected_country = st.sidebar.selectbox("Select Country",country)
    
    medal_tally = helper.fetch_medal_tally(df,selected_year,selected_country)
    
    #For making Title of the data viewed
    if selected_year == 'Overall' and selected_country == 'Overall':
        st.title("Overall Tally")
    if selected_year != 'Overall' and selected_country == 'Overall':
        st.title("Medal Tally in " + str(selected_year))
    if selected_year == 'Overall' and selected_country != 'Overall':
        st.title("Medal Tally of " + selected_country)
    if selected_year != 'Overall' and selected_country != 'Overall':
        st.title("Medla Tally of " + selected_country + " in " + str(selected_year))            

    st.dataframe(medal_tally)  

if user_menu == 'Overall Analysis':
    editions = df['Year'].unique().shape[0]-1
    cities = df['City'].unique().shape[0]
    sports = df['Sport'].unique().shape[0]
    events = df['Event'].unique().shape[0]
    athlets = df['Name'].unique().shape[0]
    nations = df['region'].unique().shape[0]


    st.title("Top Stastics") 
    col1,col2,col3 = st.columns(3)
    with col1:
        st.header("Editions")
        st.title(editions)
    with col2:
        st.header("Hosts")  
        st.title(cities)
    with col3:
        st.header("sports")      
        st.title(sports)

    col1,col2,col3 = st.columns(3)
    with col1:
        st.header("Events")
        st.title(events)
    with col2:
        st.header("Nations")  
        st.title(nations)
    with col3:
        st.header("Athletes")      
        st.title(athlets)    

