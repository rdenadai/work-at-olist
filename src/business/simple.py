from datetime import datetime


def check_phone_number(number):
    number = str(number) if not isinstance(number, str) else number
    size = len(number)
    if 10 <= size <= 11:
        for n in number:
            if n not in [str(m) for m in range(0, 10)]:
                return False
        return True
    else:
        return False


def check_timestamp(timestamp):
    timestamp = str(timestamp) if not isinstance(timestamp, str) else timestamp
    try:
        datetime.fromtimestamp(float(timestamp))
        return True
    except ValueError:
        return False
    except TypeError:
        return False


def check_reference_period(period):
    year = datetime.now().year
    period = str(period) if not isinstance(period, str) else period
    try:
        period = [int(p) for p in period.split('/')]
        if len(period) == 2:
            if 1 <= period[0] <= 12 and 1970 <= period[1] <= year:
                return True
            else:
                return False
        else:
            return False
    except ValueError:
        return False
    except TypeError:
        return False
