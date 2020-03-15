import boto3
from boto3.dynamodb.conditions import Key, Attr
from todos.src.exceptions import NotFoundException

class Todo(object):
    def __init__(self, id='', todo=''):
        self.id = id
        self.todo = todo


class TodoCRUD(object):
    def __init__(self, dynamodb_table=''):
        dynamodb = boto3.resource('dynamodb')
        self.table = dynamodb.Table(dynamodb_table)

    def get(self, id):
        result = self.table.query(KeyConditionExpression=Key('id').eq(id))
        if result['Count'] == 0:
            raise NotFoundException("Key '{}' not found".format(id))

        return result

    def list(self):
        result = self.table.scan()
        return result

    def create(self, todo):
        result = self.table.put_item(
            Item={
                "id": todo.id,
                "todo": todo.todo
            }
        )
        return result

    def update(self, todo):
        delete_res = self.delete(todo.id)
        result = self.create(todo)
        return result

    def delete(self, id):
        result = self.get(id)
        items = result['Items']
        result = [self.table.delete_item(Key=item) for item in items]
        return result
