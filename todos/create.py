import json
import boto3


def create(event, context):
    dynamodb = boto3.resource('dynamodb')
    print(event)

    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response