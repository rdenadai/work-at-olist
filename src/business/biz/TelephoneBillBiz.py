from datetime import datetime
from .TelephoneBiz import TelephoneBiz
from ..verifiers import TelephoneBillVerifier
from ..biz.BillBiz import BillBiz
from ..biz.CallBiz import CallBiz
from ..rules import convert_strtime_to_time, convert_low_time_to_big
from ...database import db_conn


class TelephoneBillBiz:

    def __init__(self, req_data, resp_data):
        self.req_data = TelephoneBillVerifier.normalize_field_values(req_data)
        self.resp_data = resp_data

    def save(self):
        self.resp_data['status'] = 406
        self.resp_data['message'] = 'Not Acceptable : Please verify if all fields and values are correct.'

        problem = False

        missing_fields = TelephoneBillVerifier.check_for_all_fields(self.req_data)
        if len(missing_fields) > 0:
            problem = True
            self.resp_data['status'] = 409
            self.resp_data['message'] = 'Conflict : Missing fields in your request, check the docs.'

        wrong_field_values = TelephoneBillVerifier.validate_fields_values(self.req_data)
        if len(wrong_field_values) > 0:
            problem = True
            self.resp_data['status'] = 409
            self.resp_data['message'] = 'Conflict : Wrong field values in your request, check the docs.'

        if not problem:
            with db_conn.atomic():
                telephone = TelephoneBiz.get_or_none(self.req_data['telephone_number'])
                if telephone:
                    period = self.req_data['reference_period']

                    result = {
                        "telephone_number":  "99999999999",
                        "reference_period":  period,
                        "total_call_price": 0.0,
                        "total_call_duration": "0h0m0s",
                        "calls": []
                    }

                    calls_id = CallBiz.get_calls_by_source(telephone.number)
                    calls_id = list(set([call.call_id for call in calls_id]))
                    bills = BillBiz.get_calls_by_period(calls_id, period)
                    ttime = {'h': 0, 'm': 0, 's': 0}
                    for bill in bills:
                        dur = convert_strtime_to_time(bill.call_duration)
                        ttime['h'] += dur[0]
                        ttime['m'] += dur[1]
                        ttime['s'] += dur[2]

                        call_start_time = bill.call_start_time
                        call_start_time = f'{call_start_time.hour}h{call_start_time.minute}m{call_start_time.second}s'

                        result['total_call_price'] += bill.call_price
                        result['calls'].append({
                            "destination": bill.destination.number,
                            "call_start_date": datetime.strftime(bill.call_start_date, '%d/%m/%Y'),
                            "call_start_time": call_start_time,
                            "call_duration": bill.call_duration,
                            "call_price": bill.call_price
                        })

                    if ttime['s'] > 60:
                        ttime['s'], ttime['m'] = convert_low_time_to_big(ttime['s'], ttime['m'])
                    if ttime['m'] > 60:
                        ttime['m'], ttime['h'] = convert_low_time_to_big(ttime['m'], ttime['h'])
                    result['total_call_duration'] = f'{ttime["h"]}h{ttime["m"]}m{ttime["s"]}s'

                    self.resp_data['result'] = result
                    self.resp_data['status'] = 201
                    self.resp_data['success'] = True
                    self.resp_data['message'] = 'Created : New call recorded in database.'
                else:
                    self.resp_data['message'] = 'Not Acceptable : Telephone number not found.'
        return self.resp_data
