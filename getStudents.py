import json
import boto3

def lambda_handler(event, context):

    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    # Select the DynamoDB table
    table = dynamodb.Table('studentData')

    # Scan the table to retrieve all items
    response = table.scan()
    data = response['Items']


    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items'])

    return data
