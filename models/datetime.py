

def high(d):
    try:
        return {'y': d.year, 'm': d.month, 'd': d.day, 'h': d.hour, 'mi': d.minute, 's': d.second,
                'ms': d.microsecond, 't': str(d.tzinfo), 'f': d.fold}
    except AttributeError:
        return {}


def mid(d):
    try:
        return {'y': d.year, 'm': d.month, 'd': d.day, 'h': d.hour, 'mi': d.minute, 's': d.second,
                'ms': d.microsecond, 't': str(d.tzinfo), 'f': d.fold}
    except AttributeError:
        return {}


def low(d):
    try:
        return {'y': d.year, 'm': d.month, 'd': d.day, 'h': d.hour, 'mi': d.minute, 's': d.second,
                'ms': d.microsecond, 'f': d.fold}
    except AttributeError:
        return {}
