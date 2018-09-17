from ..app import application
import pytest


@pytest.fixture(scope='module')
def test_client():
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


def test_call_record(test_client):
    resp = test_client.post('/call/record/', data={
        "type":  "start",
        "timestamp":  "1536939832.731359",
        "call_id":  1,
        "source":  "55994467898",
        "destination":  "55994487710"
    })
    assert resp.status_code == 200


def test_call_start(test_client):
    resp = test_client.post('/call/record/', data={
        "type":  "start",
        "timestamp":  "1536939832.731359",
        "call_id":  1,
        "source":  "55994467898",
        "destination":  "55994487710"
    })
    assert resp.status_code == 200


def test_call_end(test_client):
    resp = test_client.post('/call/end/', data={
        "type":  "end",
        "timestamp":  "1536939832.731359",
        "call_id":  1,
        "source":  "55994467898",
        "destination":  "55994487710"
    })
    assert resp.status_code == 200


def test_telephone_bill(test_client):
    resp = test_client.post('/telephone/bill/', data={
        "telephone_number":  "55994467898",
        "reference_period":  "09/2018",
    })
    assert resp.status_code == 200
