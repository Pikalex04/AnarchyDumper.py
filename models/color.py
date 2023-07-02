

def high(color):
    try:
        return {'b': color.b, 'g': color.g, 'r': color.r, 'value': color.value}
    except AttributeError:
        return 'None'


def mid(color):
    try:
        return {'b': color.b, 'g': color.g, 'r': color.r, 'value': color.value}
    except AttributeError:
        return 'None'


def low(color):
    try:
        return {'b': color.b, 'g': color.g, 'r': color.r, 'value': color.value}
    except AttributeError:
        return 'None'
