import streamlit as st
import pandas as pd

st.markdown(
        f"""
<style>
    .reportview-container .main .block-container{{
        max-width: 90%;
        padding-top: 5rem;
        padding-right: 5rem;
        padding-left: 5rem;
        padding-bottom: 5rem;
    }}
    img{{
    	max-width:40%;
    	margin-bottom:40px;
    }}
</style>
""",
        unsafe_allow_html=True,
    )




header= st.beta_container
usc_courses = st.beta_container
road_map= st.beta_container
professors =st.beta_container
functions = st.beta_container
motiv = st.beta_container

with header: 
    st.title('MADVA')
    st.header('Master\'s in Applied Data Science Vitual Advisor')
    st.subheader('By Tyler Alcorn and Chaimi Lee')
    st.write("This app that helps USC students who are pursuing a Master's degree in Applied Data Science schedule and register for DSCI courses based on their interests and degree progress.")
    


with usc_courses:
    st.title('DSCI Courses')
    #insert a table with all the coureses laid out
    #include the professors who are 
    #example with an old dataframe
    italy= pd.read_csv("Italy_dataframe.csv")
    st.write(italy.head())

with road_map:
    st.header("Road Map to Graduation")
    st.write("")

with functions:
    #if only this was the easy part
    st.header("Functions")

with motiv:
    st.title("Motivations")
    st.write("Our motivation for creating MADVA (Master's in Applied Data science Virtual Advisor) was to help our fellow Applied Data Science students avoid these obstacles and better prepare ourselves for the coming semester and achieve our career goals. This app would significantly reduce stress during registration periods and help students plan future courses based on their interests and other students' experiences. This app would also be helpful for students who have less flexible schedules due to jobs, being in a different time zone, etc. With MADVA, our goal is to ensure that current and future DSCI students make the best out of their educational journey at USC.")