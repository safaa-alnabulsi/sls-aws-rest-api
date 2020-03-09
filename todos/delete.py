import json
import boto3
import os
from boto3.dynamodb.conditions import Key, Attr

dynamodb_table = os.environ['DYNAMODB_TABLE']


def delete(event, context):
    print('Inside the delete function')

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(dynamodb_table)

    id = event['pathParameters']['id']

    result = table.query(KeyConditionExpression=Key('id').eq(id))
    items = result['Items']

    result = [table.delete_item(Key=item) for item in items]

    response = {
        "statusCode": 200,
        "body": json.dumps(result)
    }

    return response
