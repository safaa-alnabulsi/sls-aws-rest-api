import json
import boto3
import os

dynamodb_table = os.environ['DYNAMODB_TABLE']


def create(event, context):
    print('Inside the create function')

    client = boto3.client('dynamodb')

    item = json.loads(event['body'])
    id = item['id']
    content = item['todo']

    result = client.put_item(
        TableName=dynamodb_table,
        Item={
            "id": {"S": id},
            "todo": {"S": content},
        }
    )

    response = {
        "statusCode": 200,
        "body": json.dumps(result)
    }

    return response
