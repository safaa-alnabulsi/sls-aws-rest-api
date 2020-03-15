import json
import os
from todos.src.todo import Todo, TodoCRUD

dynamodb_table = os.environ['DYNAMODB_TABLE']

def create(event, context):
    item = json.loads(event['body'])
    new_todo = Todo(item['id'], item['todo'])
    result = TodoCRUD(dynamodb_table).create(new_todo)
    response = {
        "statusCode": 200,
        "body": json.dumps(result)
    }

    return response
