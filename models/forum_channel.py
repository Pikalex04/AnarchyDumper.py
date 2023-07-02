from models import category_channel, channel_flags, channel_type, datetime, forum_layout_type, forum_order_type, \
    forum_tag, guild, partial_emoji, permission_overwrite, role, thread


def high(x):
    d = {'available_tags': [forum_tag.mid(y) for y in x.available_tags],
         'category': category_channel.mid(x.category), 'category_id': x.category_id,
         'changed_roles': [role.mid(y) for y in x.changed_roles], 'created_at': datetime.mid(x.created_at),
         'default_auto_archive_duration': x.default_auto_archive_duration,
         'default_layout': forum_layout_type.mid(x.default_layout),
         'default_reaction_emoji': partial_emoji.mid(x.default_reaction_emoji),
         'default_sort_order': forum_order_type.mid(x.default_sort_order),
         'default_thread_slowmode_delay': x.default_thread_slowmode_delay, 'flags': channel_flags.mid(x.flags),
         'guild': guild.mid(x.guild), 'id': x.id, 'jump_url': x.jump_url, 'last_message_id': x.last_message_id,
         'mention': x.mention, 'name': x.name, 'nsfw': x.nsfw, 'overwrites': {},
         'permissions_synced': x.permissions_synced, 'position': x.position, 'slowmode_delay': x.slowmode_delay,
         'threads': [thread.mid(y) for y in x.threads], 'topic': x.topic, 'type': channel_type.mid(x.type)}
    for overwrite_key in x.overwrites:
        d['overwrites'][str(overwrite_key)] = permission_overwrite.low(x.overwrites[overwrite_key])
    return d


def mid(x):
    d = {'available_tags': [forum_tag.low(y) for y in x.available_tags],
         'category': category_channel.low(x.category), 'category_id': x.category_id,
         'changed_roles': [role.low(y) for y in x.changed_roles], 'created_at': datetime.low(x.created_at),
         'default_auto_archive_duration': x.default_auto_archive_duration,
         'default_layout': forum_layout_type.low(x.default_layout),
         'default_reaction_emoji': partial_emoji.low(x.default_reaction_emoji),
         'default_sort_order': forum_order_type.low(x.default_sort_order),
         'default_thread_slowmode_delay': x.default_thread_slowmode_delay, 'flags': channel_flags.low(x.flags),
         'guild': guild.low(x.guild), 'id': x.id, 'jump_url': x.jump_url, 'last_message_id': x.last_message_id,
         'mention': x.mention, 'name': x.name, 'nsfw': x.nsfw, 'overwrites': {},
         'permissions_synced': x.permissions_synced, 'position': x.position, 'slowmode_delay': x.slowmode_delay,
         'threads': [thread.low(y) for y in x.threads], 'topic': x.topic, 'type': channel_type.low(x.type)}
    for overwrite_key in x.overwrites:
        d['overwrites'][str(overwrite_key)] = permission_overwrite.low(x.overwrites[overwrite_key])
    return d


def low(x):
    return {'category_id': x.category_id, 'default_auto_archive_duration': x.default_auto_archive_duration,
            'default_thread_slowmode_delay': x.default_thread_slowmode_delay, 'id': x.id, 'jump_url': x.jump_url,
            'last_message_id': x.last_message_id, 'mention': x.mention, 'name': x.name, 'nsfw': x.nsfw,
            'permissions_synced': x.permissions_synced, 'position': x.position, 'topic': x.topic}
