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
    
    
    st.header("About You")

    class_standing=st.multiselect('Which semester are you currently in?', ['1st Semester', '2nd Semester', '3rd Semester', '4th Semester', '5th semester', 'beyond 5th semester'])

    courses_taken=st.multiselect('Which DSCI/CSCI courses have you taken so far?', ['DSCI 510', 'DSCI 529', 'DSCI 544', 'DSCI 549', 'DSCI 550', 'CSCI 550', 'DSCI 551', 'DSCI 552', 'DSCI 553', 'DSCI 554',
                                                                                    'DSCI 555', 'DSCI 556', 'DSCI 558', 'DSCI 560', 'DSCI 564', 'CSCI 570', 'CSCI 572', 'CSCI 587', 'DSCI 599'])                                                                               
    interests=st.multiselect('What are your data science interests?', ['Natural Language Processing (NLP)', 'Data Visualization', 'Algorithms', 'Data Mining',
                                                                       'Machine Learning (ML)', 'Database Systems', 'Artificial Intelligence (AI)', 'Data Management', 'Probability and Statistics'])
    #st.write('You selected: ', interests)

if __name__ == '__main__':
    main()