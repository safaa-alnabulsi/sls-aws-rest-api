import json
import boto3
import os

dynamodb_table = os.environ['dynamodbTable']


def create(event, context):
    print('Inside the create function')

    client = boto3.client('dynamodb')

    item = json.loads(event['body'])
    id = item['id']
    content = item['todo']

    response = client.put_item(
        TableName=dynamodb_table,
        Item={
            "id": {"S": id},
            "todo": {"S": content},
        }
    )

    body = {
        "message": "PutItem succeeded!",
        "input": json.dumps(response)
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response