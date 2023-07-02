from models import asset


async def high(x):
    try:
        return {'cover': await asset.mid(x.cover, f'message_application__cover__{x.id}'), 'description': x.description,
                'icon': await asset.mid(x.icon, f'message_application__icon__{x.id}'), 'id': x.id, 'name': x.name}
    except AttributeError:
        return 'None'


def mid(x):
    try:
        return {'cover': asset.low(x.cover), 'description': x.description, 'icon': asset.low(x.icon), 'id': x.id,
                'name': x.name}
    except AttributeError:
        return 'None'


def low(x):
    try:
        return {'description': x.description, 'id': x.id, 'name': x.name}
    except AttributeError:
        return 'None'
