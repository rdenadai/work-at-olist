from peewee import *
from ..database import db_conn


class Telephone(Model):
    number = CharField(primary_key=True, unique=True, index=True, max_length=11)
    name = CharField(max_length=100)

    class Meta:
        database = db_conn
        table_name = 'telephone'


class Call(Model):
    type = CharField(max_length=5)
    timestamp = TimestampField()
    call_id = IntegerField(index=True)
    source = ForeignKeyField(Telephone, index=True)
    destination = ForeignKeyField(Telephone)

    class Meta:
        database = db_conn
        table_name = 'call'
        indexes = (
            # create a unique on type/call_id/source
            (('type', 'call_id', 'source'), True),
        )


class Bill(Model):
    call_id = IntegerField(index=True)
    destination = ForeignKeyField(Telephone, index=True)
    call_start_date = DateField()
    call_start_time = TimeField()
    call_duration = CharField(max_length=50)
    call_price = FloatField()

    class Meta:
        database = db_conn
        table_name = 'bill'
