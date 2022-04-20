import boto3
import boto3.dynamodb.conditions as conditions
from botocore.exceptions import ClientError


client = boto3.client(
    'dynamodb',
    region_name= 'us-west-1',
    aws_access_key_id='AKIA6EBMFI674ZVBGZW7',
    aws_secret_access_key='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',
    )
dynamodb = boto3.resource(
    'dynamodb',
    region_name= 'us-west-1',
    aws_access_key_id='AKIA6EBMFI674ZVBGZW7',
    aws_secret_access_key='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',
    )
ddb_exceptions = client.exceptions

# try:
#     table = client.create_table(
#         TableName='MADVA',
#         KeySchema=[
#             {
#                 'AttributeName': 'PK',
#                 'KeyType': 'HASH'
#             },
#             {
#                 'AttributeName': 'SK',
#                 'KeyType': 'RANGE'
#             }
#         ],
#         AttributeDefinitions=[
#             {
#                 'AttributeName': 'PK',
#                 'AttributeType': 'S'
#             },
#             {
#                 'AttributeName': 'SK',
#                 'AttributeType': 'S'
#             }
    
#         ],
#         ProvisionedThroughput={
#             'ReadCapacityUnits': 40,
#             'WriteCapacityUnits': 20
#         }
#     )
#     print("Creating table")
#     waiter = client.get_waiter('table_exists')
#     waiter.wait(TableName='MADVA')
#     print("Table created")
    
# except ddb_exceptions.ResourceInUseException:
#     print("Table exists")


table= dynamodb.Table('MADVA')

# table.put_item(Item={
# "PK":"USC_Students",
# "SK":"chaimile@usc.edu",
# "Background":"Mathematics",
# "Class standing":"2nd Semester",
# "Graduating":"No",
# "Waived courses":[
# "None"
# ],
# "Courses taken":{
# "1":[
# "DSCI 510",
# "DSCI 549"
# ],
# "2":[
# "DSCI 550",
# "DSCI 551"
# ],
# },
# "Interests":[
# "Algorithms",
# "Data Analysis",
# "Big Data"
# ]
# }
# )

table.put_item(Item={
"PK":"USC_Students",
"SK":"tyleralc@usc.edu",
"Background":"Physics",
"Class standing":"2nd Semester",
"Graduating":"No",
"Waived courses":[
"None"
],
"Courses taken":{
"1":[
"DSCI 510",
"DSCI 549"
],
"2":[
"DSCI 550",
"DSCI 551"
]
},
"Interests":[
"Algorithms",
"Data Analysis",
"Big Data",
"Data Modeling",
"Data Processing"
]
})














reviews= [  {
            "PK":"USC_Course",
            "SK":"DSCI 510",
            "Review":"worst class ever!!!",
            "Recommend":"No"
            },
            {
            "PK":"USC_Course",
            "SK" :"DSCI 510",
            "Review":"decent",
            "Recommend":"Yes"
            }
        ]



# for j in reviews:
#     table.put_item(Item=j, UpdateExpression="SET Review = list_append(Review, j['Review')") 

#     pk=j['PK']
#     sk=j['SK']



#     try:
#             table.update_item(
#                 Key={
#                     "PK":"USC_Course",
#                     "SK":"DSCI 510",
#                 },
#                 UpdateExpression="SET #r = list_append(#r, :review_)",
#                 ExpressionAttributeNames={
#                     "#r": "Review",
#                 },
#                 ExpressionAttributeValues={
#                     ":review_": [review_]
#                 },
#                 ConditionExpression=conditions.Attr("PK","SK").exists()

#             )
#     except ClientError as err:
#         if err.response["Error"]["Code"] == 'ConditionalCheckFailedException':
#             raise ValueError("Sensor doesn't exist") from err
#         else:
#             raise err