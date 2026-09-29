from datetime import datetime


def validate_date(date):

    try:
        datetime.strptime(
            date,
            "%d/%m/%Y")

        return True

    except ValueError:
        return False


def validate_number(value):

    try:
        number = int(value)

        if number > 0:
            return True

        else:
            return False

    except ValueError:
        return False