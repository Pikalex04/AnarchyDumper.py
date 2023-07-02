from models import channel_type, datetime, guild


def high(x):
    return {'created_at': datetime.mid(x.created_at), 'guild': guild.mid(x.guild), 'guild_id': x.guild_id,
            'id': x.id, 'jump_url': x.jump_url, 'type': channel_type.mid(x.type)}


def mid(x):
    return {'created_at': datetime.low(x.created_at), 'guild': guild.low(x.guild), 'guild_id': x.guild_id,
            'id': x.id, 'jump_url': x.jump_url, 'type': channel_type.low(x.type)}


def low(x):
    return {'guild_id': x.guild_id, 'id': x.id, 'jump_url': x.jump_url}
