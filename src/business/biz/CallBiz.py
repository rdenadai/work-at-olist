from datetime import datetime
from .TelephoneBiz import TelephoneBiz
from ..rules import CallVerifier
from ...models.models import Call
from ...database import db_conn


class CallBiz:

    def __init__(self, req_data, resp_data):
        self.req_data = CallVerifier.normalize_field_values(req_data)
        self.resp_data = resp_data

    def save(self):
        self.resp_data['status'] = 406
        self.resp_data['message'] = 'Not Acceptable : Please verify if all fields and values are correct.'

        missing_fields = CallVerifier.check_for_all_fields(self.req_data)
        if len(missing_fields) > 0:
            self.resp_data['status'] = 409
            self.resp_data['message'] = 'Conflict : Missing fields in your request, check the docs.'

        wrong_field_values = CallVerifier.validate_fields_values(self.req_data)
        if len(wrong_field_values) > 0:
            self.resp_data['status'] = 409
            self.resp_data['message'] = 'Conflict : Wrong field values in your request, check the docs.'

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
                    self.resp_data['status'] = 201
                    self.resp_data['success'] = True
                    self.resp_data['message'] = 'Created : New call recorded in database.'
        return self.resp_data

    @staticmethod
    def get_or_none(id):
        return CallBiz.get_or_none(id=id)

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
