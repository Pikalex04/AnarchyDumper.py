from models import datetime, guild, role, user


def high(x):
    return {'animated': x.animated, 'available': x.available, 'created_at': datetime.mid(x.created_at),
            'guild': guild.mid(x.guild), 'guild_id': x.guild_id, 'id': x.id, 'managed': x.managed, 'name': x.name,
            'require_colons': x.require_colons, 'roles': [role.mid(y) for y in x.roles], 'url': x.url,
            'user': user.mid(x.user)}


def mid(x):
    return {'animated': x.animated, 'available': x.available, 'created_at': datetime.low(x.created_at),
            'guild': guild.low(x.guild), 'guild_id': x.guild_id, 'id': x.id, 'managed': x.managed, 'name': x.name,
            'require_colons': x.require_colons, 'roles': [role.low(y) for y in x.roles], 'url': x.url,
            'user': user.low(x.user)}


def low(x):
    return {'animated': x.animated, 'available': x.available, 'guild_id': x.guild_id, 'id': x.id, 'managed': x.managed,
            'name': x.name, 'require_colons': x.require_colons, 'url': x.url}
