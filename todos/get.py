import json
import boto3
import os

dynamodb_table = os.environ['DYNAMODB_TABLE']

def get(event, context):
    print('Inside the get function')
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(dynamodb_table)
    print(event)
    id = event['pathParameters']['id']
    print(id)
    result = table.get_item(
        Key={
            'id': id
        }
    )

    response = {
        "statusCode": 200,
        "body": json.dumps(result)
    }

    return response
