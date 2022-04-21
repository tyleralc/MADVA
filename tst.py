import requests
import json

response = requests.get('https://project-practice-8f9b2-default-rtdb.firebaseio.com/.json?orderBy="$key"')
churned_dict=response.json()
print(churned_dict)




def get_email(course_name):

    has_taken_class=[]
    #get all the names of all_courses line 325 
    if course_name in churned_dict['Courses taken']:
        has_taken_class.append(course_name)
    
    #f'{}@usc.edu'

    pass


    # get studets who have similiar interests to you 


