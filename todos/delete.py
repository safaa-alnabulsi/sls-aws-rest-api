import json
import boto3
import os

dynamodb_table = os.environ['DYNAMODB_TABLE']

def delete(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(dynamodb_table)

    item = json.loads(event['body'])
    id = item['id']
    content = item['todo']

    result = table.delete_item(
        Key={
            "id": id,
            "todo": content
        }
    )

    response = {
        "statusCode": 200,
        "body": json.dumps(result)
    }

    return response
