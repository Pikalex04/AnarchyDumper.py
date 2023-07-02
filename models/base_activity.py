from models import datetime


def high(x):
    return {'created_at': datetime.mid(x.created_at)}


def mid(x):
    return {'created_at': datetime.low(x.created_at)}


def low():
    return {}
