import json
import os
from todos.src.todo import Todo, TodoCRUD

dynamodb_table = os.environ['DYNAMODB_TABLE']

def update(event, context):
    item = json.loads(event['body'])
    updated_todo = Todo(item['id'], item['todo'])
    result = TodoCRUD(dynamodb_table).update(updated_todo)
    response = {
        "statusCode": 200,
        "body": json.dumps(result)
    }

    return response


    # You cannot update the value of hash-key, you will have to delete and recreate the item.
    # the relevant aws documentation http://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_AttributeValueUpdate.html
    # the following call will add a new atrribute, val, instead of updating the todo attr.
    # result = table.update_item(
    #     Key=old_item,
    #     UpdateExpression='SET #todo = :val',
    #     ConditionExpression=Attr('id').eq(id),
    #     ExpressionAttributeNames={'#todo': 'val'},
    #     ExpressionAttributeValues={':val': todo_text},
    #     ReturnValues="UPDATED_NEW"
    # )
