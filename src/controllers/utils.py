from time import time
from functools import wraps
from flask import Response
import rapidjson
from src.business.biz.CallBiz import CallBiz


def api_data_return():
    def intern_dec(func):
        @wraps(func)
        def wrapper_decorator(*args, **kwargs):
            start = time()
            data = {
                'status': 405,
                'success': False,
                'execution_time': 0,
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
        status=data['status'],
        mimetype='application/json'
    )


def call_request(data, request, type=None):
    if request.method == 'POST':
        if request.is_json:
            try:
                req_data = request.get_json()
                if req_data:
                    # In case we are calling api start | end endpoints
                    if type:
                        req_data['type'] = type
                    data = CallBiz(req_data, data).save()
            except Exception as e:
                data['status'] = 406
                data['message'] = 'Not Acceptable : Content type must be application/json'
        else:
            data['status'] = 406
            data['message'] = 'Not Acceptable : Content type must be application/json'
    return data