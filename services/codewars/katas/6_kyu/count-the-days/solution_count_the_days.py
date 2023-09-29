from datetime import datetime

def count_days(d):
    today = datetime.now()
    total_sec = (d-today).total_seconds()
    days = round(total_sec / 86400)

    if days < -1:
        return 'The day is in the past!'
    elif days in (-1, 0):
        return 'Today is the day!'
    else:
        return f'{days} days'
