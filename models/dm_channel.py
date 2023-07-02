from models import channel_type, client_user, datetime, guild, user


def high(x):
    return {'created_at': datetime.mid(x.created_at), 'guild': guild.mid(x.guild), 'id': x.id, 'jump_url': x.jump_url,
            'me': client_user.mid(x.me), 'recipient': user.mid(x.recipient), 'type': channel_type.mid(x.type)}


def mid(x):
    return {'created_at': datetime.low(x.created_at), 'guild': guild.low(x.guild), 'id': x.id, 'jump_url': x.jump_url,
            'me': client_user.low(x.me), 'recipient': user.low(x.recipient), 'type': channel_type.low(x.type)}


def low(x):
    return {'id': x.id, 'jump_url': x.jump_url}
