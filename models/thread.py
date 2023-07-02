from models import category_channel, channel_flags, channel_type, datetime, forum_channel, forum_tag, guild, member, \
    message, text_channel, thread_member


def high(x):
    return {'applied_tags': [forum_tag.mid(y) for y in x.applied_tags],
            'archive_timestamp': datetime.mid(x.archive_timestamp), 'archived': x.archived,
            'archiver_id': x.archiver_id, 'auto_archive_duration': x.auto_archive_duration,
            'category': category_channel.mid(x.category), 'category_id': x.category_id,
            'created_at': datetime.mid(x.created_at), 'flags': channel_flags.mid(x.flags), 'guild': guild.mid(x.guild),
            'id': x.id, 'invitable': x.invitable, 'jump_url': x.jump_url, 'last_message': message.mid(x.last_message),
            'last_message_id': x.last_message_id, 'locked': x.locked, 'me': thread_member.mid(x.me),
            'member_count': x.member_count, 'members': [thread_member.mid(y) for y in x.members], 'mention': x.mention,
            'message_count': x.message_count, 'name': x.name, 'owner': member.mid(x.owner), 'owner_id': x.owner_id,
            'parent': text_channel.mid(x.parent) if str(x.afk_channel.type) == 'text' else forum_channel.mid(x.parent),
            'parent_id': x.parent_id, 'slowmode_delay': x.slowmode_delay,
            'starter_message': message.mid(x.starter_message), 'type': channel_type.mid(x.type)}


def mid(x):
    return {'applied_tags': [forum_tag.low(y) for y in x.applied_tags],
            'archive_timestamp': datetime.low(x.archive_timestamp), 'archived': x.archived,
            'archiver_id': x.archiver_id, 'auto_archive_duration': x.auto_archive_duration,
            'category': category_channel.low(x.category), 'category_id': x.category_id,
            'created_at': datetime.low(x.created_at), 'flags': channel_flags.low(x.flags), 'guild': guild.low(x.guild),
            'id': x.id, 'invitable': x.invitable, 'jump_url': x.jump_url, 'last_message': message.low(x.last_message),
            'last_message_id': x.last_message_id, 'locked': x.locked, 'me': thread_member.low(x.me),
            'member_count': x.member_count, 'members': [thread_member.low(y) for y in x.members], 'mention': x.mention,
            'message_count': x.message_count, 'name': x.name, 'owner': member.low(x.owner), 'owner_id': x.owner_id,
            'parent': text_channel.low(x.parent) if str(x.afk_channel.type) == 'text' else forum_channel.low(x.parent),
            'parent_id': x.parent_id, 'slowmode_delay': x.slowmode_delay,
            'starter_message': message.low(x.starter_message), 'type': channel_type.low(x.type)}


def low(x):
    return {'archived': x.archived, 'archiver_id': x.archiver_id, 'auto_archive_duration': x.auto_archive_duration,
            'category_id': x.category_id, 'id': x.id, 'invitable': x.invitable, 'jump_url': x.jump_url,
            'last_message_id': x.last_message_id, 'locked': x.locked, 'member_count': x.member_count,
            'mention': x.mention, 'message_count': x.message_count, 'name': x.name, 'owner_id': x.owner_id,
            'parent_id': x.parent_id, 'slowmode_delay': x.slowmode_delay}
