from models import category_channel, channel_type, datetime, guild, member, message, permission_overwrite, role, thread


def high(x):
    try:
        d = {'category': category_channel.mid(x.category), 'category_id': x.category_id,
             'changed_roles': [role.mid(y) for y in x.changed_roles], 'created_at': datetime.mid(x.created_at),
             'default_auto_archive_duration': x.default_auto_archive_duration,
             'default_thread_slowmode_delay': x.default_thread_slowmode_delay, 'guild': guild.mid(x.guild), 'id': x.id,
             'jump_url': x.jump_url, 'last_message': message.mid(x.last_message), 'last_message_id': x.last_message_id,
             'members': [member.mid(y) for y in x.members], 'mention': x.mention, 'name': x.name, 'nsfw': x.nsfw,
             'permissions_synced': x.permissions_synced, 'position': x.position, 'slowmode_delay': x.slowmode_delay,
             'threads': [thread.mid(y) for y in x.threads], 'topic': x.topic, 'type': channel_type.mid(x.type),
             'overwrites': {}}
        for overwrite_key in x.overwrites:
            d['overwrites'][str(overwrite_key)] = permission_overwrite.low(x.overwrites[overwrite_key])
        return d
    except AttributeError:
        return 'None'


def mid(x):
    try:
        d = {'category': category_channel.low(x.category), 'category_id': x.category_id,
             'changed_roles': [role.low(y) for y in x.changed_roles], 'created_at': datetime.low(x.created_at),
             'default_auto_archive_duration': x.default_auto_archive_duration,
             'default_thread_slowmode_delay': x.default_thread_slowmode_delay, 'guild': guild.low(x.guild),
             'id': x.id, 'jump_url': x.jump_url, 'last_message': message.low(x.last_message),
             'last_message_id': x.last_message_id, 'members': [member.low(y) for y in x.members],
             'mention': x.mention, 'name': x.name, 'nsfw': x.nsfw, 'overwrites': {},
             'permissions_synced': x.permissions_synced, 'position': x.position, 'slowmode_delay': x.slowmode_delay,
             'threads': [thread.low(y) for y in x.threads], 'topic': x.topic, 'type': channel_type.low(x.type)}
        for overwrite_key in x.overwrites:
            d['overwrites'][str(overwrite_key)] = permission_overwrite.low(x.overwrites[overwrite_key])
        return d
    except AttributeError:
        return 'None'


def low(x):
    try:
        return {'category_id': x.category_id, 'default_auto_archive_duration': x.default_auto_archive_duration,
                'default_thread_slowmode_delay': x.default_thread_slowmode_delay, 'id': x.id, 'jump_url': x.jump_url,
                'last_message_id': x.last_message_id, 'mention': x.mention, 'name': x.name, 'nsfw': x.nsfw,
                'permissions_synced': x.permissions_synced, 'position': x.position, 'slowmode_delay': x.slowmode_delay,
                'topic': x.topic}
    except AttributeError:
        return 'None'
