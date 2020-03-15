import json
import os
from todos.src.todo import TodoCRUD, NotFoundException

dynamodb_table = os.environ['DYNAMODB_TABLE']

def delete(event, context):
    id = event['pathParameters']['id']
    try:
        result = TodoCRUD(dynamodb_table).delete(id)
        response = { "statusCode": 200,  "body": json.dumps(result)}
    except NotFoundException as e:
        response = { "statusCode": 404,  "body": str(e)}

    return response
