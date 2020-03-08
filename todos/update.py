import json
import boto3
import os

dynamodb_table = os.environ['DYNAMODB_TABLE']


def update(event, context):
    print('Inside the update function')

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(dynamodb_table)

    item = json.loads(event['body'])
    id = item['id']
    content = item['todo']

    result = table.update_item(
        TableName=dynamodb_table,
        Key={
            'id': id,
        },
        ExpressionAttributeNames={
            '#todo': 'todo',
        },
        ExpressionAttributeValues={
            ':todo': content,
        },
        UpdateExpression='SET #todo = :todo',
        ReturnValues='ALL_NEW',
    )

    response = {
        "statusCode": 200,
        "body": json.dumps(result)
    }

    return response
