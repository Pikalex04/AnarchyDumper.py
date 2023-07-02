from models import asset, color, datetime, guild, member, permissions, role_tags


async def high(x):
    return {'color': color.mid(x.color), 'colour': color.mid(x.colour), 'created_at': datetime.mid(x.created_at),
            'display_icon': await asset.mid(x.display_icon, f'role__display_icon__{x.id}'),
            'guild': await guild.mid(x.guild), 'hoist': x.hoist, 'icon': await asset.mid(x.icon, f'role__icon__{x.id}'),
            'id': x.id, 'managed': x.managed, 'members': [member.mid(y) for y in x.members], 'mention': x.mention,
            'mentionable': x.mentionable, 'name': x.name, 'permissions': permissions.mid(x.permissions),
            'position': x.position, 'tags': role_tags.mid(x.tags), 'unicode_emoji': x.unicode_emoji}


def mid(x):
    return {'color': color.low(x.color), 'colour': color.low(x.colour), 'created_at': datetime.low(x.created_at),
            'display_icon': asset.low(x.display_icon), 'guild': guild.low(x.guild), 'hoist': x.hoist,
            'icon': asset.low(x.icon), 'id': x.id, 'managed': x.managed, 'members': [member.low(y) for y in x.members],
            'mention': x.mention, 'mentionable': x.mentionable, 'name': x.name,
            'permissions': permissions.low(x.permissions), 'position': x.position, 'tags': role_tags.low(x.tags),
            'unicode_emoji': x.unicode_emoji}


def low(x):
    return {'hoist': x.hoist, 'id': x.id, 'managed': x.managed, 'mention': x.mention, 'mentionable': x.mentionable,
            'name': x.name, 'position': x.position, 'unicode_emoji': x.unicode_emoji}
