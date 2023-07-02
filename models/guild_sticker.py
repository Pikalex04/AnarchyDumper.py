from models import guild, sticker_format_type, user


def high(x):
    return {'available': x.available, 'description': x.description, 'emoji': x.emoji,
            'format': sticker_format_type.mid(x.format), 'guild': guild.mid(x.guild), 'guild_id': x.guild_id,
            'id': x.id, 'name': x.name, 'user': user.mid(x.user)}


def mid(x):
    return {'available': x.available, 'description': x.description, 'emoji': x.emoji,
            'format': sticker_format_type.low(x.format), 'guild': guild.low(x.guild), 'guild_id': x.guild_id,
            'id': x.id, 'name': x.name, 'user': user.low(x.user)}


def low(x):
    return {'available': x.available, 'description': x.description, 'emoji': x.emoji, 'guild_id': x.guild_id,
            'id': x.id, 'name': x.name}
