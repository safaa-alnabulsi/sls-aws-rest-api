import json
import os
from todos.src.todo import TodoCRUD

dynamodb_table = os.environ['DYNAMODB_TABLE']


def list(event, context):
    result = TodoCRUD(dynamodb_table).list()
    return {
        "statusCode": 200,
        "body": json.dumps(result)
    }
