import json
import os
from todos.src.todo import Todo, TodoCRUD
from todos.src.exceptions import NotFoundException
from todos.src.utils import exp_handler

dynamodb_table = os.environ['DYNAMODB_TABLE']

@exp_handler
def update(event, context):
    item = json.loads(event['body'])
    updated_todo = Todo(item['id'], item['todo'])
    result = TodoCRUD(dynamodb_table).update(updated_todo)
    return {
        "statusCode": 200,
        "body": json.dumps(result)
    }
