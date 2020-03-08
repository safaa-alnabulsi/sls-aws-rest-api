import json
import boto3
import os

dynamodb_table = os.environ['DYNAMODB_TABLE']

def list(event, context):
    print('Inside the list function')

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(dynamodb_table)

    result = table.scan()

    response = {
        "statusCode": 200,
        "body": json.dumps(result)
    }

    return response
