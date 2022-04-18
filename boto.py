import boto3

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

try:
    table = client.create_table(
        TableName='MADVA',
        KeySchema=[
            {
                'AttributeName': 'PK',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'SK',
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'PK',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'SK',
                'AttributeType': 'S'
            }
    
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 40,
            'WriteCapacityUnits': 20
        }
    )
    print("Creating table")
    waiter = client.get_waiter('table_exists')
    waiter.wait(TableName='MADVA')
    print("Table created")
    
except ddb_exceptions.ResourceInUseException:
    print("Table exists")