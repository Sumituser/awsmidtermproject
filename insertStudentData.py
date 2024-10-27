import json
import boto3

#DynamoDB object using the AWS SDK
dynamodb = boto3.resource('dynamodb')
# DynamoDB object to select our table
table = dynamodb.Table('studentData')

# Handler function that the Lambda service will use as an entry point
def lambda_handler(event, context):

    student_id = event['studentid']
    name = event['name']
    student_class = event['class']
    age = event['age']
    

    response = table.put_item(
        Item={
            'studentid': student_id,
            'name': name,
            'class': student_class,
            'age': age
        }
    )
    

    return {
        'statusCode': 200,
        'body': json.dumps('Student data saved successfully!')
    }
