from models import button_style, component_type, partial_emoji


def high(x):
    return {'custom_id': x.custom_id, 'disabled': x.disabled, 'emoji': partial_emoji.mid(x.emoji), 'label': x.label,
            'style': button_style.mid(x.style), 'type': component_type.mid(x.type), 'url': x.url}


def mid(x):
    return {'custom_id': x.custom_id, 'disabled': x.disabled, 'emoji': partial_emoji.low(x.emoji), 'label': x.label,
            'style': button_style.low(x.style), 'type': component_type.low(x.type), 'url': x.url}


def low(x):
    return {'custom_id': x.custom_id, 'disabled': x.disabled, 'label': x.label, 'url': x.url}
