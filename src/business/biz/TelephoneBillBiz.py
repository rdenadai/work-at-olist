from .TelephoneBiz import TelephoneBiz
from ..rules import TelephoneBillVerifier
from ...database import db_conn


class TelephoneBillBiz:

    def __init__(self, req_data, resp_data):
        self.req_data = TelephoneBillVerifier.normalize_field_values(req_data)
        self.resp_data = resp_data

    def save(self):
        self.resp_data['status'] = 406
        self.resp_data['message'] = 'Not Acceptable : Please verify if all fields and values are correct.'

        missing_fields = TelephoneBillVerifier.check_for_all_fields(self.req_data)
        if len(missing_fields) > 0:
            self.resp_data['status'] = 409
            self.resp_data['message'] = 'Conflict : Missing fields in your request, check the docs.'

        wrong_field_values = TelephoneBillVerifier.validate_fields_values(self.req_data)
        if len(wrong_field_values) > 0:
            self.resp_data['status'] = 409
            self.resp_data['message'] = 'Conflict : Wrong field values in your request, check the docs.'

        with db_conn.atomic():
            telephone = TelephoneBiz.get_or_none(self.req_data['telephone_number'])
            if telephone:
                self.resp_data['status'] = 201
                self.resp_data['success'] = True
                self.resp_data['message'] = 'Created : New call recorded in database.'
            else:
                self.resp_data['message'] = 'Not Acceptable : Telephone number not found.'
        return self.resp_data
