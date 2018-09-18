from datetime import datetime, timedelta
from ..settings import TARIF_VALUE, STANDING_CHARGE


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


def calculate_tarif(call_start, call_end):
    duration = call_end - call_start
    minutes = int(duration.seconds / 60)
    t_minutes = (duration.days * 3600) + minutes
    tarif = STANDING_CHARGE
    dt_start = call_start
    for _ in range(0, t_minutes):
        if dt_start.hour == 6 and dt_start.minute >= 0 and dt_start.second >= 0:
            tarif += TARIF_VALUE

        dt_start = (dt_start + timedelta(minutes=1))
        if 6 < dt_start.hour < 22:
            tarif += TARIF_VALUE
        elif dt_start.hour == 22 and dt_start.minute == 0 and dt_start.second == 0:
            tarif += TARIF_VALUE

    return round(tarif, 2)


def calculate_total_call_duration(call_start, call_end):
    duration = call_end - call_start
    hours = int(duration.seconds / 3600)
    minutes = int(duration.seconds / 60) % 60
    seconds = duration.seconds - (60 * minutes + hours * 3600)
    return f'{hours}h{minutes}m{seconds}s'


def convert_strtime_to_time(time_f):
    for k in ['h', 'm', 's']:
        time_f = time_f.replace(k, '|')
    return [int(k) for k in time_f.split('|') if k]


def convert_low_time_to_big(low, big):
    lt = low
    bg = int(lt / 60) % 60
    big += bg
    low = lt - (bg * 60)
    return low, big