from time import time
from datetime import datetime


telephone_source_data = {
    'number': '99999999999',
    'name': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
}
telephone_destination_data = {
    'number': '99999999998',
    'name': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXY'
}
telephone_bill_data = {
    "telephone_number":  "99999999999",
    "reference_period":  "09/2018",
}
call_data = {
    'type': 'start',
    'timestamp': time(),
    'call_id': 1,
    'source': None,
    'destination': None,
}
bill_data = {
    'destination': None,
    'call_start_date': datetime.now(),
    'call_start_time': datetime.now().time(),
    'call_duration': '0h35m42s',
    'call_price': 3.96,
}
bill_history_data = {
    'destination': None,
    'reference_month': datetime.now(),
    'total_minutes': 2,
    'total_amount': 0.54
}
