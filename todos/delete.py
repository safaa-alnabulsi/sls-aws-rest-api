import json
import os
from todos.src.todo import TodoCRUD
from todos.src.exceptions import NotFoundException
from todos.src.utils import exp_handler

dynamodb_table = os.environ['DYNAMODB_TABLE']


@exp_handler
def delete(event, context):
    id = event['pathParameters']['id']
    result = TodoCRUD(dynamodb_table).delete(id)
    return {
        "statusCode": 200,
        "body": json.dumps(result)
    }
