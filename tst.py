import requests
import json

response = requests.get('https://project-practice-8f9b2-default-rtdb.firebaseio.com/.json?orderBy="$key"')
churned_dict=response.json()
print(churned_dict)
