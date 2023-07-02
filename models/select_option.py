from models import partial_emoji


def high(x):
    return {'default': x.default, 'description': x.description, 'emoji': partial_emoji.mid(x), 'label': x.label,
            'value': x.value}


def mid(x):
    return {'default': x.default, 'description': x.description, 'emoji': partial_emoji.low(x), 'label': x.label,
            'value': x.value}


def low(x):
    return {'default': x.default, 'description': x.description, 'label': x.label, 'value': x.value}
