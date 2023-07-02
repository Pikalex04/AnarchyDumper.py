from models import abc_guild_channel, channel_type, datetime, guild, permission_overwrite, role, stage_channel, \
    text_channel, voice_channel


def high(x):
    d = {'category': mid(x.category), 'changed_roles': [role.mid(y) for y in x.changed_roles],
         'channels': [abc_guild_channel.mid(y) for y in x.channels], 'created_at': datetime.mid(x.created_at),
         'guild': guild.mid(x.guild), 'id': x.id, 'jump_url': x.jump_url, 'mention': x.mention, 'name': x.name,
         'nsfw': x.nsfw, 'overwrites': {}, 'permissions_synced': x.permissions_synced,
         'position': x.position, 'stage_channels': [stage_channel.mid(y) for y in x.stage_channels],
         'text_channels': [text_channel.mid(y) for y in x.text_channels], 'type': channel_type.mid(x.type),
         'voice_channels': [voice_channel.mid(y) for y in x.voice_channels]}
    for overwrite_key in x.overwrites:
        d['overwrites'][str(overwrite_key)] = permission_overwrite.mid(x.overwrites[overwrite_key])
    return d


def mid(x):
    d = {'category': low(x.category), 'changed_roles': [role.low(y) for y in x.changed_roles],
         'channels': [abc_guild_channel.low(y) for y in x.channels], 'created_at': datetime.low(x.created_at),
         'guild': guild.low(x.guild), 'id': x.id, 'jump_url': x.jump_url, 'mention': x.mention, 'name': x.name,
         'nsfw': x.nsfw, 'overwrites': {}, 'permissions_synced': x.permissions_synced,
         'position': x.position, 'stage_channels': [stage_channel.low(y) for y in x.stage_channels],
         'text_channels': [text_channel.low(y) for y in x.text_channels], 'type': channel_type.low(x.type),
         'voice_channels': [voice_channel.low(y) for y in x.voice_channels]}
    for overwrite_key in x.overwrites:
        d['overwrites'][str(overwrite_key)] = permission_overwrite.low(x.overwrites[overwrite_key])
    return d


def low(x):
    return {'id': x.id, 'jump_url': x.jump_url, 'mention': x.mention, 'name': x.name,
            'nsfw': x.nsfw, 'permissions_synced': x.permissions_synced, 'position': x.position}
