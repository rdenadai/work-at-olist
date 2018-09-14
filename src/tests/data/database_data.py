from time import time
from datetime import datetime


telephone_source_data = {
    'number': '55999999999',
    'name': 'XXXXXXXXXXXXXXXXXXXXXXX'
}
telephone_destination_data = {
    'number': '55999999998',
    'name': 'XXXXXXXXXXXXXXXXXXXXXXX'
}
call_data = {
    'type': 'start',
    'timestamp': time(),
    'call_id': 70,
    'source': None,
    'destination': None,
}
bill_data = {
    'owner': None,
    'reference_month': datetime.now(),
    'total_minutes': 2,
    'total_amount': 0.54
}
