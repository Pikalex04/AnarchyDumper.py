from models import datetime, interaction_type, member, user


def high(x):
    try:
        d = {'created_at': datetime.mid(x.created_at), 'id': x.id, 'name': x.name, 'type': interaction_type.mid(x.type)}
        try:
            d['user'] = member.mid(x.user)
        except AttributeError:
            d['user'] = user.mid(x.user)
        return d
    except AttributeError:
        return 'None'


def mid(x):
    try:
        d = {'created_at': datetime.low(x.created_at), 'id': x.id, 'name': x.name, 'type': interaction_type.low(x.type)}
        try:
            d['user'] = member.low(x.user)
        except AttributeError:
            d['user'] = user.low(x.user)
        return d
    except AttributeError:
        return 'None'


def low(x):
    try:
        return {'id': x.id, 'name': x.name}
    except AttributeError:
        return 'None'
