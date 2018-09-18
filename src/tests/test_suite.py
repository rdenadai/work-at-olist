from datetime import datetime, timedelta
from ..business.rules import CallVerifier, TelephoneBillVerifier
from ..business.simple import check_phone_number
from ..business.simple import check_timestamp
from ..business.simple import check_reference_period
from ..business.simple import calculate_tarif
from ..business.simple import calculate_total_call_duration
from ..business.simple import convert_strtime_to_time
from ..business.simple import convert_low_time_to_big


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
    assert len(TelephoneBillVerifier.validate_fields_values(data)) <= 0


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


def test_calculate_tarif():
    dates = [
        (datetime.strptime('17/09/2018 10:11:15', '%d/%m/%Y %H:%M:%S'),
         datetime.strptime('17/09/2018 10:16:12', '%d/%m/%Y %H:%M:%S'), .72),
        (datetime.strptime('21/02/2017 06:01:00', '%d/%m/%Y %H:%M:%S'),
         datetime.strptime('21/02/2017 06:02:00', '%d/%m/%Y %H:%M:%S'), .45),
        (datetime.strptime('15/10/2017 21:59:00', '%d/%m/%Y %H:%M:%S'),
         datetime.strptime('15/10/2017 22:17:15', '%d/%m/%Y %H:%M:%S'), .45),
        (datetime.strptime('17/09/2018 21:57:13', '%d/%m/%Y %H:%M:%S'),
         datetime.strptime('17/09/2018 22:17:53', '%d/%m/%Y %H:%M:%S'), .54),
        (datetime.strptime('31/12/2018 23:05:15', '%d/%m/%Y %H:%M:%S'),
         datetime.strptime('01/01/2019 01:11:15', '%d/%m/%Y %H:%M:%S'), .36),
        (datetime.strptime('17/09/2018 05:59:15', '%d/%m/%Y %H:%M:%S'),
         datetime.strptime('17/09/2018 06:05:15', '%d/%m/%Y %H:%M:%S'), .81),
        (datetime.strptime('17/09/2018 05:59:15', '%d/%m/%Y %H:%M:%S'),
         datetime.strptime('17/09/2018 06:59:15', '%d/%m/%Y %H:%M:%S'), 5.67),
        (datetime.strptime('17/09/2018 07:01:15', '%d/%m/%Y %H:%M:%S'),
         datetime.strptime('17/09/2018 12:01:45', '%d/%m/%Y %H:%M:%S'), 27.36),
        (datetime.fromtimestamp(1537298435.420377),
         datetime.fromtimestamp(1537472762.381068), 434.61),
        (datetime.strptime('16/09/2018 06:00:00', '%d/%m/%Y %H:%M:%S'),
         datetime.strptime('17/09/2018 22:00:00', '%d/%m/%Y %H:%M:%S'), 281.52),
    ]

    for date in dates:
        call_start_dt = date[0]
        call_end_dt = date[1]
        tarif = date[2]
        assert calculate_tarif(call_start_dt, call_end_dt) == tarif


def test_calculate_total_call_duration():
    dates = [
        (datetime.strptime('17/09/2018 10:11:15', '%d/%m/%Y %H:%M:%S'),
         datetime.strptime('17/09/2018 10:16:15', '%d/%m/%Y %H:%M:%S'), '0h5m0s'),
        (datetime.strptime('21/02/2017 06:01:00', '%d/%m/%Y %H:%M:%S'),
         datetime.strptime('21/02/2017 06:02:00', '%d/%m/%Y %H:%M:%S'), '0h1m0s'),
        (datetime.strptime('15/10/2017 21:59:00', '%d/%m/%Y %H:%M:%S'),
         datetime.strptime('15/10/2017 22:17:15', '%d/%m/%Y %H:%M:%S'), '0h18m15s'),
        (datetime.strptime('17/09/2018 21:57:13', '%d/%m/%Y %H:%M:%S'),
         datetime.strptime('17/09/2018 22:17:53', '%d/%m/%Y %H:%M:%S'), '0h20m40s'),
        (datetime.strptime('31/12/2018 23:05:15', '%d/%m/%Y %H:%M:%S'),
         datetime.strptime('01/01/2019 01:11:15', '%d/%m/%Y %H:%M:%S'), '2h6m0s'),
        (datetime.strptime('17/09/2018 05:59:15', '%d/%m/%Y %H:%M:%S'),
         datetime.strptime('17/09/2018 06:05:15', '%d/%m/%Y %H:%M:%S'), '0h6m0s'),
        (datetime.strptime('17/09/2018 05:59:15', '%d/%m/%Y %H:%M:%S'),
         datetime.strptime('17/09/2018 06:59:15', '%d/%m/%Y %H:%M:%S'), '1h0m0s'),
        (datetime.strptime('17/09/2018 07:01:15', '%d/%m/%Y %H:%M:%S'),
         datetime.strptime('17/09/2018 12:01:45', '%d/%m/%Y %H:%M:%S'), '5h0m30s'),
    ]

    for date in dates:
        call_start_dt = date[0]
        call_end_dt = date[1]
        ttime = date[2]
        assert calculate_total_call_duration(call_start_dt, call_end_dt) == ttime


def test_sum_bills_time():
    ttime = {'h': 0, 'm': 0, 's': 0}
    for dt in ['0h50m10s', '1h10m50s', '0h25m10s']:
        dur = convert_strtime_to_time(dt)
        ttime['h'] += dur[0]
        ttime['m'] += dur[1]
        ttime['s'] += dur[2]
    if ttime['s'] > 60:
        ttime['s'], ttime['m'] = convert_low_time_to_big(ttime['s'], ttime['m'])
    if ttime['m'] > 60:
        ttime['m'], ttime['h'] = convert_low_time_to_big(ttime['m'], ttime['h'])
    assert ttime['h'] == 2 and ttime['m'] == 26 and ttime['s'] == 10
