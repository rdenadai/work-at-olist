import pytest
import rapidjson
from ..app import application
from .data.database_data import *
from .test_database import clean_data


@pytest.fixture(scope='module')
def flask_test_client():
    """Boilerplate to create a Flask app for testing."""
    flask_app = application
    # Flask provides a way to test your application by exposing the Werkzeug test Client
    # and handling the context locals for you.
    testing_client = flask_app.test_client()
    # Establish an application context before running the tests.
    ctx = flask_app.app_context()
    ctx.push()
    yield testing_client  # this is where the testing happens!
    ctx.pop()


def test_call_record(flask_test_client):
    clean_data()
    data = call_data.copy()
    data['source'] = telephone_source_data['number']
    data['destination'] = telephone_destination_data['number']
    resp = flask_test_client.post('/call/record/', data=rapidjson.dumps(data), content_type='application/json')
    assert resp.status_code == 201
    assert rapidjson.loads(resp.data)['status'] == 201
    clean_data()


def test_call_record_406(flask_test_client):
    clean_data()
    data = call_data.copy()
    data['source'] = telephone_source_data['number']
    data['destination'] = telephone_destination_data['number']
    resp = flask_test_client.post('/call/record/', data='abc', content_type='application/json')
    assert resp.status_code == 406
    assert rapidjson.loads(resp.data)['status'] == 406
    clean_data()


def test_call_start(flask_test_client):
    clean_data()
    data = call_data.copy()
    data['source'] = telephone_source_data['number']
    data['destination'] = telephone_destination_data['number']
    resp = flask_test_client.post('/call/start/', data=rapidjson.dumps(data), content_type='application/json')
    assert resp.status_code == 201
    assert rapidjson.loads(resp.data)['status'] == 201
    clean_data()


def test_call_end(flask_test_client):
    clean_data()
    data = call_data.copy()
    data['source'] = telephone_source_data['number']
    data['destination'] = telephone_destination_data['number']
    resp = flask_test_client.post('/call/end/', data=rapidjson.dumps(data), content_type='application/json')
    assert resp.status_code == 201
    assert rapidjson.loads(resp.data)['status'] == 201
    clean_data()


def test_telephone_bill(flask_test_client):
    resp = flask_test_client.post('/telephone/bill/', data={
        "telephone_number":  "55994467898",
        "reference_period":  "09/2018",
    })
    assert resp.status_code == 405
