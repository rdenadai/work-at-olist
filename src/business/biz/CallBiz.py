from datetime import datetime
import calendar
from ..simple import calculate_tarif, calculate_total_call_duration
from .BillBiz import BillBiz
from .TelephoneBiz import TelephoneBiz
from ..rules import CallVerifier
from ...models.models import Call, Bill
from ...database import db_conn


class CallBiz:

    def __init__(self, req_data, resp_data):
        self.req_data = CallVerifier.normalize_field_values(req_data)
        self.resp_data = resp_data

    @staticmethod
    def get_or_none(id):
        return CallBiz.get_or_none(id=id)

    @staticmethod
    def get_calls_by_source(source):
        return Call.select().where(Call.source == source)

    @staticmethod
    def get_calls_by_period(period):
        period = str(period) if not isinstance(period, str) else period
        period = [int(p) for p in period.split('/')]
        last_day = calendar.monthrange(period[1], period[0])[1]
        start = datetime.strptime(f'01/{period[0]}/{period[1]}', '%d/%m/%Y')
        end = datetime.strptime(f'{last_day}/{period[0]}/{period[1]}', '%d/%m/%Y')
        return Call.select().where(Call.timestamp.between(start.timestamp(), end.timestamp()))

    @staticmethod
    def save_call_end(destination, call_id):
        call_start = Call.get_or_none(type='start', call_id=call_id)
        call_end = Call.get_or_none(type='end', call_id=call_id)
        if call_start and call_end:
            t_duration = calculate_total_call_duration(call_start.timestamp, call_end.timestamp)
            tarif = calculate_tarif(call_start.timestamp, call_end.timestamp)

            model = Bill(
                call_id=call_id,
                destination=destination,
                call_start_date=call_start.timestamp.date(),
                call_start_time=call_start.timestamp.time(),
                call_duration=t_duration,
                call_price=tarif)
            if BillBiz.save(model):
                return True
        return False

    def save(self):
        self.resp_data['status'] = 406
        self.resp_data['message'] = 'Not Acceptable : Please verify if all fields and values are correct.'

        problem = False

        missing_fields = CallVerifier.check_for_all_fields(self.req_data)
        if len(missing_fields) > 0:
            problem = True
            self.resp_data['status'] = 409
            self.resp_data['message'] = 'Conflict : Missing fields in your request, check the docs.'

        wrong_field_values = CallVerifier.validate_fields_values(self.req_data)
        if len(wrong_field_values) > 0:
            problem = True
            self.resp_data['status'] = 409
            self.resp_data['message'] = 'Conflict : Wrong field values in your request, check the docs.'

        if not problem:
            with db_conn.atomic():
                source = TelephoneBiz().save_and_get(self.req_data['source'])
                destination = TelephoneBiz().save_and_get(self.req_data['destination'])
                if source and destination:
                    call_model = Call()
                    call_model.type = self.req_data['type']
                    call_model.timestamp = datetime.fromtimestamp(float(self.req_data['timestamp']))
                    call_model.call_id = self.req_data['call_id']
                    call_model.source = source
                    call_model.destination = destination
                    mod = call_model.save(force_insert=True)
                    if mod > 0:
                        CallBiz.save_call_end(call_model.destination, call_model.call_id)
                        self.resp_data['status'] = 201
                        self.resp_data['success'] = True
                        self.resp_data['message'] = 'Created : New call recorded in database.'
        return self.resp_data

    def save_and_get(self):
        missing_fields = CallVerifier.check_for_all_fields(self.req_data)
        if len(missing_fields) > 0:
            return None
        wrong_field_values = CallVerifier.validate_fields_values(self.req_data)
        if len(wrong_field_values) > 0:
            return None

        with db_conn.atomic():
            source = TelephoneBiz().save_and_get(self.req_data['source'])
            destination = TelephoneBiz().save_and_get(self.req_data['destination'])
            if source and destination:
                call_model = Call()
                call_model.type = self.req_data['type']
                call_model.timestamp = datetime.fromtimestamp(float(self.req_data['timestamp']))
                call_model.call_id = self.req_data['call_id']
                call_model.source = source
                call_model.destination = destination
                mod = call_model.save(force_insert=True)
                if mod > 0:
                    return CallBiz.get_or_none(call_model.id)
        return None
