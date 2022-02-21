import streamlit as st
import pandas as pd
import sys
from lxml import etree
import requests



def main():


    header= st.beta_container
    usc_courses = st.beta_container
    road_map= st.beta_container
    professors =st.beta_container
    functions = st.beta_container
    motiv = st.beta_container

    # with header:
    st.title('MADVA')
    st.header('Master\'s in Applied Data Science Vitual Advisor')
    st.subheader('By Tyler Alcorn and Chaimi Lee')
    st.write("This an app that helps USC students who are pursuing a Master's degree in Applied Data Science schedule and register for DSCI courses based on their interests and degree progress.")
    
    # with usc_courses: get the courses dataframe 
    st.header('DSCI Courses')
    html = pd.read_html('https://classes.usc.edu/term-20221/classes/dsci/', header = 0)
    courses = html[0]
    st.write(courses)

    # with road_map:
    st.header("Road Map to Graduation")
    st.write("")

    # with functions:
    
    st.header("Functions")

    # with motiv:
    st.header("Motivations")
    st.write("Our motivation for creating MADVA (Master's in Applied Data science Virtual Advisor) was to help our fellow Applied Data Science students avoid these obstacles and better prepare ourselves for the coming semester and achieve our career goals. This app would significantly reduce stress during registration periods and help students plan future courses based on their interests and other students' experiences. This app would also be helpful for students who have less flexible schedules due to jobs, being in a different time zone, etc. With MADVA, our goal is to ensure that current and future DSCI students make the best out of their educational journey at USC.")


if __name__ == '__main__':
    main()