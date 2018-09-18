from .rules import check_phone_number, check_timestamp, check_reference_period


class Verifier:

    keys = []

    @classmethod
    def check_for_all_fields(self, data):
        missing_fields = []
        for key in self.keys:
            if key not in data:
                missing_fields += [key]
        return missing_fields


class CallVerifier(Verifier):

    keys = ['type', 'timestamp', 'call_id', 'source', 'destination']

    @classmethod
    def normalize_field_values(self, data):
        data['type'] = str(data.get('type', ''))
        data['timestamp'] = str(data.get('timestamp', ''))
        data['source'] = str(data.get('source', ''))
        data['destination'] = str(data.get('destination', ''))

        data['call_id'] = str(data.get('call_id', 0))
        for dot in ['.', ',']:
            data['call_id'] = data['call_id'].replace(dot, '')
        data['call_id'] = int(data['call_id'])
        return data

    @classmethod
    def validate_fields_values(self, data):
        wrong_field_value = []
        for key, value in data.items():
            if key == 'type' and (value not in ['start', 'end']):
                wrong_field_value += [key]
            elif key == 'source' and not check_phone_number(value):
                wrong_field_value += [key]
            elif key == 'destination' and not check_phone_number(value):
                wrong_field_value += [key]
            elif key == 'timestamp' and not check_timestamp(value):
                wrong_field_value += [key]
        return wrong_field_value


class TelephoneBillVerifier(Verifier):

    keys = ['telephone_number']

    @classmethod
    def normalize_field_values(self, data):
        data['telephone_number'] = str(data.get('telephone_number', ''))
        data['reference_period'] = str(data.get('reference_period', ''))
        return data

    @classmethod
    def validate_fields_values(self, data):
        wrong_field_value = []
        for key, value in data.items():
            if key == 'telephone_number' and not check_phone_number(value):
                wrong_field_value += [key]
            if key == 'reference_period' and not check_reference_period(value):
                wrong_field_value += [key]
        return wrong_field_value
