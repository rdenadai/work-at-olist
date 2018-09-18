import requests
import rapidjson
from datetime import datetime
from .settings import CONFIG


if __name__ == '__main__':
    data = [
        {
            'type': 'start',
            'timestamp': datetime.strptime('2016-02-29 12:00:00', '%Y-%m-%d %H:%M:%S').timestamp(),
            'call_id': 70,
            'source': 99988526423,
            'destination': 9993468278,
        }, {
            'type': 'end',
            'timestamp': datetime.strptime('2016-02-29 14:00:00', '%Y-%m-%d %H:%M:%S').timestamp(),
            'call_id': 70,
            'source': 99988526423,
            'destination': 9993468278,
        }, {
            'type': 'start',
            'timestamp': datetime.strptime('2017-12-12 15:07:13', '%Y-%m-%d %H:%M:%S').timestamp(),
            'call_id': 71,
            'source': 99988526423,
            'destination': 9993468278,
        }, {
            'type': 'end',
            'timestamp': datetime.strptime('2017-12-12 15:14:56', '%Y-%m-%d %H:%M:%S').timestamp(),
            'call_id': 71,
            'source': 99988526423,
            'destination': 9993468278,
        }, {
            'type': 'start',
            'timestamp': datetime.strptime('2017-12-12 22:47:56', '%Y-%m-%d %H:%M:%S').timestamp(),
            'call_id': 72,
            'source': 99988526423,
            'destination': 9993468278,
        }, {
            'type': 'end',
            'timestamp': datetime.strptime('2017-12-12 22:50:56', '%Y-%m-%d %H:%M:%S').timestamp(),
            'call_id': 72,
            'source': 99988526423,
            'destination': 9993468278,
        }, {
            'type': 'start',
            'timestamp': datetime.strptime('2017-12-12 21:57:13', '%Y-%m-%d %H:%M:%S').timestamp(),
            'call_id': 73,
            'source': 99988526423,
            'destination': 9993468278,
        }, {
            'type': 'end',
            'timestamp': datetime.strptime('2017-12-12 22:10:56', '%Y-%m-%d %H:%M:%S').timestamp(),
            'call_id': 73,
            'source': 99988526423,
            'destination': 9993468278,
        }, {
            'type': 'start',
            'timestamp': datetime.strptime('2017-12-12 04:57:13', '%Y-%m-%d %H:%M:%S').timestamp(),
            'call_id': 74,
            'source': 99988526423,
            'destination': 9993468278,
        }, {
            'type': 'end',
            'timestamp': datetime.strptime('2017-12-12 06:10:56', '%Y-%m-%d %H:%M:%S').timestamp(),
            'call_id': 74,
            'source': 99988526423,
            'destination': 9993468278,
        }, {
            'type': 'start',
            'timestamp': datetime.strptime('2017-12-12 21:57:13', '%Y-%m-%d %H:%M:%S').timestamp(),
            'call_id': 75,
            'source': 99988526423,
            'destination': 9993468278,
        }, {
            'type': 'end',
            'timestamp': datetime.strptime('2017-12-12 22:10:56', '%Y-%m-%d %H:%M:%S').timestamp(),
            'call_id': 75,
            'source': 99988526423,
            'destination': 9993468278,
        }, {
            'type': 'start',
            'timestamp': datetime.strptime('2017-12-12 15:07:58', '%Y-%m-%d %H:%M:%S').timestamp(),
            'call_id': 76,
            'source': 99988526423,
            'destination': 9993468278,
        }, {
            'type': 'end',
            'timestamp': datetime.strptime('2017-12-12 15:12:56', '%Y-%m-%d %H:%M:%S').timestamp(),
            'call_id': 76,
            'source': 99988526423,
            'destination': 9993468278,
        }, {
            'type': 'start',
            'timestamp': datetime.strptime('2018-02-28 21:57:13', '%Y-%m-%d %H:%M:%S').timestamp(),
            'call_id': 77,
            'source': 99988526423,
            'destination': 9993468278,
        }, {
            'type': 'end',
            'timestamp': datetime.strptime('2018-02-28 22:10:56', '%Y-%m-%d %H:%M:%S').timestamp(),
            'call_id': 77,
            'source': 99988526423,
            'destination': 9993468278,
        }
    ]

    for d in data:
        r = requests.post(f'{CONFIG.URL}/call/record/', data=rapidjson.dumps(d), headers={'Content-Type': 'application/json'})
