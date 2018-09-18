from flask import (Blueprint, request)
from .utils import api_data_return, call_request, telephone_bill_request


api = Blueprint('api', __name__)


@api.route('/call/record/', methods=['POST'])
@api_data_return()
def call_record(data):
    return call_request(data, request)


@api.route('/call/start/', methods=['POST'])
@api_data_return()
def call_start(data):
    return call_request(data, request, type='start')


@api.route('/call/end/', methods=['POST'])
@api_data_return()
def call_end(data):
    return call_request(data, request, type='end')


@api.route('/telephone/bill/', methods=['GET', 'POST'])
@api_data_return()
def get_telephone_bill(data):
    return telephone_bill_request(data, request)
