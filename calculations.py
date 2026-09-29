from datetime import datetime, timedelta


def calculate_next_period(last_period, cycle_length):

    date = datetime.strptime(
        last_period,
        "%d/%m/%Y")

    next_period = date + timedelta(
        days=cycle_length)

    return next_period.strftime(
        "%d/%m/%Y")


def calculate_cycle_day(last_period):

    date = datetime.strptime(
        last_period,
        "%d/%m/%Y")

    today = datetime.today()

    cycle_day = (today - date).days + 1

    return cycle_day