from ..business.rules import CallVerifier, BillVerifier
from ..business.simple import check_phone_number, check_timestamp, check_reference_period


def test_call_verifier_all_fields():
    data = {
        "type": "start",
        "timestamp": "1536939832.731359",
        "call_id": 70,
        "source": "55994467898",
        "destination": "55994487710"
    }
    assert len(CallVerifier.check_for_all_fields(data)) <= 0


def test_call_verifier_missing_fields():
    data = {
        "timestamp": "1536939832.731359",
        "call_id": 70,
        "destination": "55994487710"
    }
    assert len(CallVerifier.check_for_all_fields(data)) > 0


def test_call_verifier_normalize_field_call_id():
    data = {
        "type": 0,
        "timestamp": 1536939832.73,
        "call_id": None,
        "source": 55994467898,
        "destination": "55994487710"
    }

    values = [70, 70.1, 70_1, '7.0', '7,0', '7,.0']
    for value in values:
        data['call_id'] = value
        data = CallVerifier.normalize_field_values(data)
        assert isinstance(data['call_id'], int)


def test_call_verifier_validate_field_values():
    data = {
        "type": "start",
        "timestamp": "1536939832.731359",
        "call_id": 70,
        "source": "55994467898",
        "destination": "55994487710"
    }
    assert len(CallVerifier.validate_fields_values(data)) <= 0


def test_bill_verifier_validate_field_values():
    data = {
        "telephone_number": "55994467898"
    }
    assert len(BillVerifier.validate_fields_values(data)) <= 0


def test_phone_number():
    numbers = [55994467898, '55994467898', '5599446789']
    for number in numbers:
        assert check_phone_number(number)
    assert not check_phone_number('545dfda7892')
    assert not check_phone_number('545dfdaSWQE32R37892')
    assert not check_phone_number('545d')


def test_timestamp():
    for timestamp in [1536939832.731359, '1536939832.731359', 1536939832.7313, '1536939832.7313', '14092018']:
        assert check_timestamp(timestamp)
    assert not check_timestamp('ajdafdsjfgj')
    assert not check_timestamp('1409sd2018')


def test_reference_period():
    for period in ['09/2018']:
        assert check_reference_period(period)
    assert not check_reference_period('2018/09')
    assert not check_reference_period(2018)
    assert not check_reference_period('abc/ashgh')
    assert not check_reference_period('01/dsfdj')
    assert not check_reference_period('dsfas/1970')
    assert not check_reference_period('01/1950')
