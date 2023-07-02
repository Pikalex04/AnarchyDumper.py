from models import category_channel, channel_type, datetime, guild, member, message, permission_overwrite, role, \
    scheduled_event, video_quality_mode


def high(x):
    d = {'bitrate': x.bitrate, 'category': category_channel.mid(x.category), 'category_id': x.category_id,
         'changed_roles': [role.mid(y) for y in x.roles], 'created_at': datetime.mid(x.created_at),
         'guild': guild.mid(x.guild), 'id': x.id, 'jump_url': x.jump_url,
         'last_message': message.mid(x.last_message), 'last_message_id': x.last_message_id,
         'members': [member.mid(y) for y in x.members], 'mention': x.mention, 'name': x.name, 'nsfw': x.nsfw,
         'overwrites': {}, 'permissions_synced': x.permissions_synced, 'position': x.position,
         'rtc_region': x.rtc_region, 'scheduled_events': [scheduled_event.mid(y) for y in x.scheduled_events],
         'slowmode_delay': x.slowmode_delay, 'type': channel_type.mid(x.type), 'user_limit': x.user_limit,
         'video_quality_mode': video_quality_mode.mid(x.video_quality_mode), 'voice_states': x.voice_states}
    for overwrite_key in x.overwrites:
        d['overwrites'][str(overwrite_key)] = permission_overwrite.low(x.overwrites[overwrite_key])
    return d


def mid(x):
    d = {'bitrate': x.bitrate, 'category': category_channel.low(x.category), 'category_id': x.category_id,
         'changed_roles': [role.low(y) for y in x.roles], 'created_at': datetime.low(x.created_at),
         'guild': guild.low(x.guild), 'id': x.id, 'jump_url': x.jump_url,
         'last_message': message.low(x.last_message), 'last_message_id': x.last_message_id,
         'members': [member.low(y) for y in x.members], 'mention': x.mention, 'name': x.name, 'nsfw': x.nsfw,
         'overwrites': {}, 'permissions_synced': x.permissions_synced, 'position': x.position,
         'rtc_region': x.rtc_region, 'scheduled_events': [scheduled_event.low(y) for y in x.scheduled_events],
         'slowmode_delay': x.slowmode_delay, 'type': channel_type.low(x.type), 'user_limit': x.user_limit,
         'video_quality_mode': video_quality_mode.low(x.video_quality_mode), 'voice_states': x.voice_states}
    for overwrite_key in x.overwrites:
        d['overwrites'][str(overwrite_key)] = permission_overwrite.low(x.overwrites[overwrite_key])
    return d


def low(x):
    return {'bitrate': x.bitrate, 'category_id': x.category_id, 'id': x.id, 'jump_url': x.jump_url,
            'last_message_id': x.last_message_id, 'mention': x.mention, 'name': x.name, 'nsfw': x.nsfw,
            'permissions_synced': x.permissions_synced, 'position': x.position, 'rtc_region': x.rtc_region,
            'slowmode_delay': x.slowmode_delay, 'user_limit': x.user_limit, 'voice_states': x.voice_states}
