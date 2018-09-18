from .data.database_data import *
from ..models.models import Telephone, Call, Bill


def clean_data():
    q = Call.delete().where(Call.source == telephone_source_data['number'])
    q.execute()
    q = Call.delete().where(Call.source == telephone_destination_data['number'])
    q.execute()
    q = Bill.delete().where(Bill.call_id == bill_data['call_id'])
    q.execute()
    q = Telephone.delete().where(Telephone.number == telephone_source_data['number'])
    q.execute()
    q = Telephone.delete().where(Telephone.number == telephone_destination_data['number'])
    q.execute()


def get_telephone(data):
    Telephone.create(**data)
    return Telephone.get_or_none(**data)


# TESTS
# ---------

def test_insert_telephone():
    clean_data()
    assert get_telephone(telephone_source_data)
    clean_data()


def test_insert_call():
    clean_data()
    call_data['source'] = get_telephone(telephone_source_data)
    call_data['destination'] = get_telephone(telephone_destination_data)
    Call.create(**call_data)
    assert Call.get_or_none(**call_data)
    clean_data()


def test_insert_bill():
    clean_data()
    bill_data['destination'] = get_telephone(telephone_source_data)
    Bill.create(**bill_data)
    assert Bill.get_or_none(**bill_data)
    clean_data()

