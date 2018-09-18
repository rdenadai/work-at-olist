from datetime import datetime
import calendar
from ...models.models import Bill


class BillBiz:

    @staticmethod
    def get_or_none(number):
        return Bill.get_or_none(number=number)

    @staticmethod
    def get_calls_by_period(calls_id, period):
        period = str(period) if not isinstance(period, str) else period
        period = [int(p) for p in period.split('/')]
        last_day = calendar.monthrange(period[1], period[0])[1]
        start = datetime.strptime(f'01/{period[0]}/{period[1]}', '%d/%m/%Y')
        end = datetime.strptime(f'{last_day}/{period[0]}/{period[1]}', '%d/%m/%Y')
        return Bill.select().where(
            Bill.call_id.in_(calls_id),
            Bill.call_start_date.between(start, end))

    @staticmethod
    def save(model):
        mod = model.save(force_insert=True)
        if mod > 0:
            return True
        return False
