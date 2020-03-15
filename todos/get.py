import json
import os
from todos.src.todo import TodoCRUD

dynamodb_table = os.environ['DYNAMODB_TABLE']

def get(event, context):
    id = event['pathParameters']['id']
    result = TodoCRUD(dynamodb_table).get(id)
    response = {
        "statusCode": 200,
        "body": json.dumps(result)
    }

    return response
