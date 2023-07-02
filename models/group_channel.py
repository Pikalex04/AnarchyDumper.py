from models import asset, channel_type, client_user, datetime, guild, member, user


async def high(x):
    return {'created_at': datetime.mid(x.created_at), 'guild': guild.mid(x.guild),
            'icon': await asset.mid(x.icon, f'group_channel__icon__{x.id}'), 'id': x.id, 'jump_url': x.jump_url,
            'me': client_user.mid(x.me), 'name': x.name, 'owner': member.mid(x.owner), 'owner_id': x.owner_id,
            'recipients': [user.mid(y) for y in x.recipients], 'type': channel_type.mid(x.type)}


def mid(x):
    return {'created_at': datetime.low(x.created_at), 'guild': guild.low(x.guild), 'icon': asset.low(x.icon),
            'id': x.id, 'jump_url': x.jump_url, 'me': client_user.low(x.me), 'name': x.name,
            'owner': member.low(x.owner), 'owner_id': x.owner_id, 'recipients': [user.low(y) for y in x.recipients],
            'type': channel_type.low(x.type)}


def low(x):
    return {'id': x.id, 'jump_url': x.jump_url, 'name': x.name, 'owner_id': x.owner_id}
