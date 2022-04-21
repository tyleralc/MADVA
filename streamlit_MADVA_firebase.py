#!/usr/bin/env python
# coding: utf-8

# In[22]:


import streamlit as st
import pandas as pd
import sys
from lxml import etree
import requests
import json
from bs4 import BeautifulSoup
import random

def about_ADSCI():
    content = requests.get('https://catalogue.usc.edu/preview_program.php?catoid=14&poid=17593&returnto=5199')
    soup = BeautifulSoup(content.content, 'html.parser')
    list_of_info=[]
    for data in soup.find_all("p"):
        list_of_info.append(data.get_text())

    string=''
    for sentence in list_of_info[12:]:
        string=string+sentence+'\n'
    string=string+'\nDepartment email: '+list_of_info[10]
    
    return string

def pd_to_list(pd_object):
    pd_object=pd_object.to_dict('split')
    pd_list=pd_object['data'][0]
    return pd_list

def DSCI_courses(year,semester,subject):
    
    df=pd.DataFrame(columns=['Course Name',"Section", "Type", "Time", "Days", "Registered", "Instructor"])

    if semester=='Spring':
        semester=1
    elif semester=='Summer':
        semester=2
    elif semester=='Fall':
        semester=3

    content = requests.get('https://classes.usc.edu/term-'+str(year)+str(semester)+'/classes/'+str(subject)+'/')
    soup = BeautifulSoup(content.content, 'html.parser')

    course_table=soup.find_all("div", class_="course-id")

    course_names=[]
    for course_element in course_table:
        name=course_element.find("a", class_="courselink")
        course_names.append(name.get_text())
    df['Course Name']=course_names
    
    html = pd.read_html('https://classes.usc.edu/term-'+str(year)+str(semester)+'/classes/'+str(subject)+'/', header = 0)
    
    list_of_data=[]
    for index in range(len(html)):
        x=html[index].loc[:,["Section", "Type", "Time", "Days", "Registered", "Instructor"]]
        list_of_data.append(pd_to_list(x))
    
    #transpose this list of lists
    list_of_data_transposed=[]
    for index_1 in range(len(list_of_data[0])):
        list_of_elements=[]
        for index_2 in range(len(list_of_data)):            
            list_of_elements.append(list_of_data[index_2][index_1])
        list_of_data_transposed.append(list_of_elements)
    
    #now put into dataframe
    df["Section"]=list_of_data_transposed[0]
    df["Type"]=list_of_data_transposed[1]
    df["Time"]=list_of_data_transposed[2]
    df["Days"]=list_of_data_transposed[3]
    df["Registered"]=list_of_data_transposed[4]
    df["Instructor"]=list_of_data_transposed[5]
    
    return df

def get_list_of_courses_offered(pandas_df):
    course_names=pandas_df['Course Name'].tolist()
    course_num=[]

    for course in course_names:
        course=course.split(':')[0]
        if "Crosslist" in course:
            course=course.replace("Crosslist ","")
        course_num.append(course)
    
    return course_num

#create dict of courses and their info
#needs get_list_of_courses_offered
def course_info_dict(year,semester,subject,pandas_df):

    if semester=='Spring':
        semester=1
    elif semester=='Summer':
        semester=2
    elif semester=='Fall':
        semester=3
        
    content = requests.get('https://classes.usc.edu/term-'+str(year)+str(semester)+'/classes/'+str(subject)+'/') #change this
    soup = BeautifulSoup(content.content, 'html.parser')

    course_info=soup.find_all("div", class_="course-details")


    course_info_list=[]
    for course_element in course_info:
        info=course_element.find("div", class_="catalogue")
        course_info_list.append(info.get_text())

    list_of_courses=get_list_of_courses_offered(pandas_df)

    course_info_dict={}

    for index in range(len(list_of_courses)):
        course_info_dict[list_of_courses[index]]=course_info_list[index]
        
    return course_info_dict

def first_sem():
    courses_taken_dict={}
    courses_list_indiv=['None','DSCI 510', 'DSCI 529', 'DSCI 544', 'DSCI 549', 'DSCI 550', 'CSCI 550', 'DSCI 551','DSCI 552','DSCI 553','DSCI 554','DSCI 555', 'DSCI 556', 'DSCI 558', 'DSCI 560','DSCI 561','DSCI 562', 'DSCI 564', 'CSCI 570', 'CSCI 572', 'CSCI 587', 'DSCI 599','Other']
    courses_taken_1=st.multiselect('Which DSCI/CSCI courses have you taken during your first semester?',courses_list_indiv, default=['None'])
    courses_taken_dict[1]=courses_taken_1
    
    return courses_taken_dict

def second_sem():
    courses_taken_dict={}
    courses_list_indiv=['None','DSCI 510', 'DSCI 529', 'DSCI 544', 'DSCI 549', 'DSCI 550', 'CSCI 550', 'DSCI 551','DSCI 552','DSCI 553','DSCI 554','DSCI 555', 'DSCI 556', 'DSCI 558', 'DSCI 560','DSCI 561','DSCI 562', 'DSCI 564', 'CSCI 570', 'CSCI 572', 'CSCI 587', 'DSCI 599','Other']
    courses_taken_1=st.multiselect('Which DSCI/CSCI courses have you taken during your first semester?',courses_list_indiv, default=['None'])
    courses_taken_dict[1]=courses_taken_1

    #for element in courses_taken_1:
       # if element != 'Other' or element != 'None':
           # courses_list_indiv.remove(element)
    courses_taken_2=st.multiselect('Which DSCI/CSCI courses have you taken during your second semester?',courses_list_indiv, default=['None'])
    courses_taken_dict[2]=courses_taken_2
    return courses_taken_dict

def third_sem():
    courses_taken_dict={}
    courses_list_indiv=['None','DSCI 510', 'DSCI 529', 'DSCI 544', 'DSCI 549', 'DSCI 550', 'CSCI 550', 'DSCI 551','DSCI 552','DSCI 553','DSCI 554','DSCI 555', 'DSCI 556', 'DSCI 558', 'DSCI 560','DSCI 561','DSCI 562', 'DSCI 564', 'CSCI 570', 'CSCI 572', 'CSCI 587', 'DSCI 599','Other']
    courses_taken_1=st.multiselect('Which DSCI/CSCI courses have you taken during your first semester?',courses_list_indiv, default=['None'])
    courses_taken_dict[1]=courses_taken_1

            
    courses_taken_2=st.multiselect('Which DSCI/CSCI courses have you taken during your second semester?',courses_list_indiv, default=['None'])
    courses_taken_dict[2]=courses_taken_2

            
    courses_taken_3=st.multiselect('Which DSCI/CSCI courses have you taken during your third semester?',courses_list_indiv, default=['None'])
    courses_taken_dict[3]=courses_taken_3
    
    return courses_taken_dict

def fourth_sem():
    courses_taken_dict={}
    courses_list_indiv=['None','DSCI 510', 'DSCI 529', 'DSCI 544', 'DSCI 549', 'DSCI 550', 'CSCI 550', 'DSCI 551','DSCI 552','DSCI 553','DSCI 554','DSCI 555', 'DSCI 556', 'DSCI 558', 'DSCI 560','DSCI 561','DSCI 562', 'DSCI 564', 'CSCI 570', 'CSCI 572', 'CSCI 587', 'DSCI 599','Other']
    courses_taken_1=st.multiselect('Which DSCI/CSCI courses have you taken during your first semester?',courses_list_indiv, default=['None'])
    courses_taken_dict[1]=courses_taken_1

            
    courses_taken_2=st.multiselect('Which DSCI/CSCI courses have you taken during your second semester?',courses_list_indiv, default=['None'])
    courses_taken_dict[2]=courses_taken_2

            
    courses_taken_3=st.multiselect('Which DSCI/CSCI courses have you taken during your third semester?',courses_list_indiv, default=['None'])
    courses_taken_dict[3]=courses_taken_3
            
    courses_taken_4=st.multiselect('Which DSCI/CSCI courses have you taken during your fourth semester?',courses_list_indiv, default=['None'])
    courses_taken_dict[4]=courses_taken_4   
    
    return courses_taken_dict

def fifth_sem():
    courses_taken_dict={}
    courses_list_indiv=['None','DSCI 510', 'DSCI 529', 'DSCI 544', 'DSCI 549', 'DSCI 550', 'CSCI 550', 'DSCI 551','DSCI 552','DSCI 553','DSCI 554','DSCI 555', 'DSCI 556', 'DSCI 558', 'DSCI 560','DSCI 561','DSCI 562', 'DSCI 564', 'CSCI 570', 'CSCI 572', 'CSCI 587', 'DSCI 599','Other']
    courses_taken_1=st.multiselect('Which DSCI/CSCI courses have you taken during your first semester?',courses_list_indiv, default=['None'])
    courses_taken_dict[1]=courses_taken_1
            
    courses_taken_2=st.multiselect('Which DSCI/CSCI courses have you taken during your second semester?',courses_list_indiv, default=['None'])
    courses_taken_dict[2]=courses_taken_2
            
    courses_taken_3=st.multiselect('Which DSCI/CSCI courses have you taken during your third semester?',courses_list_indiv, default=['None'])
    courses_taken_dict[3]=courses_taken_3
            
    courses_taken_4=st.multiselect('Which DSCI/CSCI courses have you taken during your fourth semester?',courses_list_indiv, default=['None'])
    courses_taken_dict[4]=courses_taken_4 

    
    courses_taken_5=st.multiselect('Which DSCI/CSCI courses have you taken during your fifth semester?',courses_list_indiv, default=['None'])
    courses_taken_dict[5]=courses_taken_5
    
    return courses_taken_dict

def beyond_fifth_sem():
    courses_taken_dict={}
    courses_list_indiv=['None','DSCI 510', 'DSCI 529', 'DSCI 544', 'DSCI 549', 'DSCI 550', 'CSCI 550', 'DSCI 551','DSCI 552','DSCI 553','DSCI 554','DSCI 555', 'DSCI 556', 'DSCI 558', 'DSCI 560','DSCI 561','DSCI 562', 'DSCI 564', 'CSCI 570', 'CSCI 572', 'CSCI 587', 'DSCI 599','Other']
    courses_taken_1=st.multiselect('Which DSCI/CSCI courses have you taken during your first semester?',courses_list_indiv, default=['None'])
    courses_taken_dict[1]=courses_taken_1
            
    courses_taken_2=st.multiselect('Which DSCI/CSCI courses have you taken during your second semester?',courses_list_indiv, default=['None'])
    courses_taken_dict[2]=courses_taken_2
            
    courses_taken_3=st.multiselect('Which DSCI/CSCI courses have you taken during your third semester?',courses_list_indiv, default=['None'])
    courses_taken_dict[3]=courses_taken_3
            
    courses_taken_4=st.multiselect('Which DSCI/CSCI courses have you taken during your fourth semester?',courses_list_indiv, default=['None'])
    courses_taken_dict[4]=courses_taken_4 

    
    courses_taken_5=st.multiselect('Which DSCI/CSCI courses have you taken during your fifth semester?',courses_list_indiv, default=['None'])
    courses_taken_dict[5]=courses_taken_5

    courses_taken_6=st.multiselect('Which DSCI/CSCI courses have you taken after your fifth semester?-- choose all courses taken since fifth semester',courses_list_indiv, default=['None'])
    courses_taken_dict[6]=courses_taken_6
    
    return courses_taken_dict

#get percentage of people who recommend a course
def how_many_recommend(course):
    response = requests.get('https://project-practice-8f9b2-default-rtdb.firebaseio.com/USC_Courses/'+str(course)+'/Recommend/.json?orderBy="$key"').json()
    recs=[]
    yes=[]
    for values in response.values():
        recs.append(values)
    for resp in recs:
        if resp=='Yes':
            yes.append(resp)
    return len(yes)/len(recs)*100

def get_reviews(course,num):
    try:
        response = requests.get('https://project-practice-8f9b2-default-rtdb.firebaseio.com/USC_Courses/'+str(course)+'/Review/.json?orderBy="$key"').json()
        reviews=[]
        for values in response.values():
            reviews.append(values)  
        leng=len(reviews)
        try:
            randomlist = random.sample(range(0, leng), num)
            
            for count,i in enumerate(randomlist):
                count_disp=count+1
                st.write(str(count_disp)+'. '+str(reviews[i]))
        except:
            st.write('Not enough info available!')
    except:
        st.write('Not enough info available!')

def get_emails(course,num):
    response = requests.get('https://project-practice-8f9b2-default-rtdb.firebaseio.com/USC_Students/.json?orderBy="$key"').json()
    emails=[]
    for key,dictionary in response.items():
        email=key+'@usc.edu'
        if course in dictionary['Courses Total']:
            emails.append(email)
    leng=len(emails)
    try:
        randomlist = random.sample(range(0, leng), num)
        print(randomlist)
        print(emails)
        
        for count,i in enumerate(randomlist):
            count_disp=count+1
            #print(str(count_disp))
            st.write(str(emails[i]))
    except:
        st.write('Not enough info available!')


def main():
    header= st.beta_container
    usc_courses = st.beta_container
    road_map= st.beta_container
    professors =st.beta_container
    functions = st.beta_container
    motiv = st.beta_container

    st.image('MADVA.png')


    st.title('MADVA: Master\'s in Applied Data Science Vitual Advisor')
    st.subheader('By Tyler Alcorn and Chaimi Lee')
    st.write("This an app that helps USC students who are pursuing a Master's degree in Applied Data Science schedule and register for DSCI courses based on their interests and degree progress.")

    st.subheader("Motivations")
    st.write("Our motivation for creating MADVA (Master's in Applied Data science Virtual Advisor) was to help our fellow Applied Data Science students avoid these obstacles and better prepare ourselves for the coming semester and achieve our career goals. This app would significantly reduce stress during registration periods and help students plan future courses based on their interests and other students\' experiences. This app would also be helpful for students who have less flexible schedules due to jobs, being in a different time zone, etc. With MADVA, our goal is to ensure that current and future DSCI students make the best out of their educational journey at USC.")

    #####
    ###get_reviews('DSCI 551',3)

    st.subheader('MS in Applied Data Science at USC')
    st.write(about_ADSCI())

    st.header('DSCI/CSCI Courses')

    year=st.radio('which year are you registering for?',('2022','2023'))
    semester=st.radio('which semester are you registering for?',('Spring','Summer','Fall'))
    subject=st.radio('Would you like to see DSCI or CSCI courses?',('DSCI','CSCI'))

    try:
        st.write('These are the courses offered in '+str(semester)+', '+str(year))
        st.write(DSCI_courses(year,semester,subject))

        course_table=DSCI_courses(year,semester,subject)
        course_offered_list=get_list_of_courses_offered(course_table)
        course_info=course_info_dict(year,semester,subject,course_table)

        course_with_info=st.selectbox('Which course would you like to get info on?', course_offered_list)
        st.write('About '+str(course_with_info))
        st.write(course_info[course_with_info])
    except:
        st.write('Course information unavailable for that term')

    st.header("About You")

    #primary key-- usc email
    usc_email_input=st.text_input('What is your USC email?: ') #use upsert incase someone wants to use this another semester

    if usc_email_input[::-1][:8]!='ude.csu@':
        st.write('Please input a valid USC email')
    usc_email=usc_email_input

    #background
    list_of_backgrounds=['Data Science','Computer Science','Engineering','Mathematics','Physics','Economics/Finance','Business','Communications','Other']
    background_info=st.selectbox('What is your undergraduate and/or professional background in?',list_of_backgrounds)

    #class standing
    class_standing=st.radio('Which semester are you currently in?', ('Incomming Student', 
                                                                     '1st Semester', '2nd Semester', '3rd Semester',
                                                                     '4th Semester', '5th Semester', 'Beyond 5th Semester'))

    if class_standing=='3rd Semester'or class_standing=='4th Semester' or class_standing=='5th semester' or class_standing=='beyond 5th semester':
        grad_or_no=st.radio('Will you be graduating after this semester?', ('Yes', 'No'))
    else:
        grad_or_no='No'

    #waied courses
    waived_courses=st.multiselect('Have you waived out of/got credit for any of these elective courses?', ['None','DSCI 510', 'DSCI 529', 'DSCI 544', 'DSCI 549', 'DSCI 550', 'CSCI 550', 'DSCI 554','DSCI 555', 'DSCI 556', 'DSCI 558', 'DSCI 560','DSCI 561','DSCI 562', 'DSCI 564', 'CSCI 570', 'CSCI 572', 'CSCI 587', 'DSCI 599','Other'])

    if class_standing=='1st Semester':
        courses_taken=first_sem()
    elif class_standing=='2nd Semester':
        courses_taken=second_sem()
    elif class_standing=='3rd Semester':
        courses_taken=third_sem()
    elif class_standing=='4th Semester':
        courses_taken=fourth_sem()
    elif class_standing=='5th Semester':
        courses_taken=fifth_sem()
    elif class_standing=='Beyond 5th Semester':
        courses_taken=beyond_fifth_sem()
    elif class_standing=='Incomming Student':
        courses_taken={}
    
    #interests
    list_of_interest=['None','Geospatial Data','Data Processing', 'Data Cleaning','Data Analysis','Big Data','Data Engineering', 'Data Analytics', 'Data Modeling','Natural Language Processing (NLP)', 'Data Visualization', 'Algorithms', 'Data Mining', 'Machine Learning (ML)', 'Database Systems', 'Artificial Intelligence (AI)', 'Data Management', 'Probability and Statistics']
    list_of_interest=sorted(list_of_interest)
    interests=st.multiselect('What are your data science interests?', list_of_interest, default=['None'])

    data_final=st.radio('Are all your inputs correct?',('No','Yes'))
    
    input_dict={}
    input_dict['Background']=background_info
    input_dict['Class standing']=class_standing
    input_dict['Graduating']=grad_or_no
    input_dict['Waived courses']=waived_courses
    input_dict['Courses taken']=courses_taken
    input_dict['Interests']=interests
    all_courses=[]
    for lists in input_dict["Courses taken"].values():
        for element in lists:
            all_courses.append(element)
    input_dict['Courses Total']=all_courses
        

    if data_final=='Yes':
        data={}
        personal_data={}
        usc_email_key=usc_email.replace('@usc.edu','')
        personal_data[usc_email_key]=input_dict
        ##this is onl for creating the first key
        #data['USC_Students']=personal_data
        #out=json.dumps(data, indent=4)
        out=json.dumps(personal_data, indent=4)
        response = requests.patch('https://project-practice-8f9b2-default-rtdb.firebaseio.com/USC_Students.json',out)
        

    #st.write(data)

    if class_standing!='Incomming Student':
        all_courses=[]
        all_reviews=[]
        for lists in input_dict["Courses taken"].values():
            for element in lists:
                all_courses.append(element)
        all_courses.append('None')

        review_or_no=st.multiselect("Would you like to leave a review about any of these courses? If so, which courses would you like to write a review about?: ",all_courses,default=[all_courses[0]])

        if review_or_no!=['None']:
            if ('None' in review_or_no):
                review_or_no.remove('None')

            reviews_list=[]
            recommend_list=[]
            for classes in review_or_no:
                
                review=st.text_input("What did you think about "+str(classes)+"?")
                recommend_or_not=st.radio("Do you recommend this course?",('Yes','No'),key=classes)
                
                reviews_list.append(review)
                recommend_list.append(recommend_or_not)
            
            review_final=st.radio('Are you sure about your reviews?',('No','Yes'))
            if review_final=='Yes':
                for index in range(len(recommend_list)):
                    classes=review_or_no[index]
                    out_1=json.dumps(reviews_list[index], indent=4)
                    out_2=json.dumps(recommend_list[index], indent=4)
                    
                    response = requests.post('https://project-practice-8f9b2-default-rtdb.firebaseio.com/USC_Courses/'+str(classes)+'/Review.json',out_1)
                    response = requests.post('https://project-practice-8f9b2-default-rtdb.firebaseio.com/USC_Courses/'+str(classes)+'/Recommend.json',out_2)

    st.header('Personalized Course Recommendation')
    st.write('Based on your background, class standing, and interests, you should take these courses next semester: ')
    if class_standing=='Incomming Student' and waived_courses==['None']:
        st.write('[DSCI 510, DSCI 549]')


    st.header('Applied DSCI Community')
    st.subheader('Reviews')
    courses_list_final=['DSCI 510', 'DSCI 529', 'DSCI 544', 'DSCI 549', 'DSCI 550', 'CSCI 550', 'DSCI 551','DSCI 552','DSCI 553','DSCI 554','DSCI 555', 'DSCI 556', 'DSCI 558', 'DSCI 560','DSCI 561','DSCI 562', 'DSCI 564', 'CSCI 570', 'CSCI 572', 'CSCI 587', 'DSCI 599']
    course=st.selectbox('Would you like to get reviews for any of these courses?', courses_list_final)
    num=st.selectbox('How many random reviews would you like to receive?',[1,2,3,4,5])

    st.write('This is what people have to say about '+str(course))
    st.write(get_reviews(course,num))
    try:
        percent=how_many_recommend(course)
        st.write(str(percent)+'% of MADVA users recommend this course')
    except:
        pass


    st.subheader('Contacts')
    course=st.selectbox('Would you like email addresses of fellow Applied DSCI students who have taken one of these courses?', courses_list_final)
    num=st.selectbox('How many random email addresses would you like to receive?',[1,2,3,4,5])

    st.write('Here are the contacts of those who have previously taken '+str(course))
    st.write(get_emails(course,num))


                
            

        
    
    #st.write('You selected: ', interests)
if __name__ == '__main__':
    main()

    
