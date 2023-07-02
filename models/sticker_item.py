from models import sticker_format_type


def high(x):
    return {'format': sticker_format_type.mid(x), 'id': x.id, 'name': x.name, 'url': x.url}


def mid(x):
    return {'format': sticker_format_type.low(x), 'id': x.id, 'name': x.name, 'url': x.url}


def low(x):
    return {'id': x.id, 'name': x.name, 'url': x.url}
