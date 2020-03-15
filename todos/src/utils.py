from todos.src.exceptions import NotFoundException

def exp_handler(func):
    def func_wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except NotFoundException as e:
            response = {"statusCode": 404, "body": str(e)}
            return response

    return func_wrapper