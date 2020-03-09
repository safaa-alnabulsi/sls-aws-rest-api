import json
import boto3
import os
from boto3.dynamodb.conditions import Key, Attr

dynamodb_table = os.environ['DYNAMODB_TABLE']


def get(event, context):
    print('Inside the get function')
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table(dynamodb_table)
    id = event['pathParameters']['id']

    result = table.query(
        KeyConditionExpression=Key('id').eq(id)
    )

    response = {
        "statusCode": 200,
        "body": json.dumps(result)
    }

    return response
