from time import time
from functools import wraps
from flask import Response
import rapidjson


def api_data_return():
    def intern_dec(func):
        @wraps(func)
        def wrapper_decorator(*args, **kwargs):
            start = time()
            data = {
                'status': 405,
                'execution_time': 0,
                'success': False,
                'message': 'Method Not Allowed',
                'result': None
            }
            data = func(data)
            data['execution_time'] = time() - start
            return format_json_response(data)
        return wrapper_decorator
    return intern_dec


def format_json_response(data):
    return Response(
        rapidjson.dumps(data),
        status=200,
        mimetype='application/json'
    )
