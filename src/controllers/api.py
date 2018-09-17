from flask import (Blueprint, request)
from .utils import api_data_return


api = Blueprint('api', __name__)


@api.route('/call/record/', methods=['POST'])
@api_data_return()
def call_record(data):
    if request.method == 'POST':
        req_data = request.get_json()
    return data


@api.route('/call/start/', methods=['POST'])
@api_data_return()
def call_start(data):
    if request.method == 'POST':
        req_data = request.get_json()
    return data


@api.route('/call/end/', methods=['POST'])
@api_data_return()
def call_end(data):
    if request.method == 'POST':
        pass
    return data


@api.route('/telephone/bill/', methods=['GET', 'POST'])
@api_data_return()
def get_telephone_bill(data):
    if request.method == 'POST':
        pass
    return data
