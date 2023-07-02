from models import partial_emoji


def high(x):
    return {'emoji': partial_emoji.mid(x.emoji), 'id': x.id, 'moderated': x.moderated, 'name': x.name}


def mid(x):
    return {'emoji': partial_emoji.low(x.emoji), 'id': x.id, 'moderated': x.moderated, 'name': x.name}


def low(x):
    return {'id': x.id, 'moderated': x.moderated, 'name': x.name}
