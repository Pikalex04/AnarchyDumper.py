from models import datetime


def high(x):
    return {'animated': x.animated, 'created_at': datetime.mid(x.created_at), 'id': x.id, 'name': x.name, 'url': x.url}


def mid(x):
    return {'animated': x.animated, 'created_at': datetime.low(x.created_at), 'id': x.id, 'name': x.name, 'url': x.url}


def low(x):
    return {'animated': x.animated, 'id': x.id, 'name': x.name, 'url': x.url}
