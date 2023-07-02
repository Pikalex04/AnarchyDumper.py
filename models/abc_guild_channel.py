from models import category_channel, datetime, guild, permission_overwrite, role


def high(x):
    d = {'category': category_channel.mid(x.category), 'changed_roles': [role.mid(y) for y in x.changed_roles],
         'created_at': datetime.mid(x.created_at), 'guild': guild.mid(x.guild), 'jump_url': x.jump_url,
         'mention': x.mention, 'name': x.name, 'overwrites': {}, 'permissions_synced': x.permissions_synced,
         'position': x.position}
    for overwrite_key in x.overwrites:
        d['overwrites'][str(overwrite_key)] = permission_overwrite.mid(x.overwrites[overwrite_key])
    return d


def mid(x):
    d = {'category': category_channel.low(x.category), 'changed_roles': [role.low(y) for y in x.changed_roles],
         'created_at': datetime.low(x.created_at), 'guild': guild.low(x.guild), 'jump_url': x.jump_url,
         'mention': x.mention, 'name': x.name, 'overwrites': {}, 'permissions_synced': x.permissions_synced,
         'position': x.position}
    for overwrite_key in x.overwrites:
        d['overwrites'][str(overwrite_key)] = permission_overwrite.low(x.overwrites[overwrite_key])
    return d


def low(x):
    return {'jump_url': x.jump_url, 'mention': x.mention, 'name': x.name, 'permissions_synced': x.permissions_synced,
            'position': x.position}
