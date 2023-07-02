from models import abc_guild_channel, abc_user, action_row, attachment, button, datetime, dm_channel, embed, \
    group_channel, guild, member, message_application, message_flags, message_interaction, message_type, \
    partial_messageable, reaction, role, role_subscription_info, select_menu, stage_channel, sticker_item, \
    text_channel, thread, voice_channel


async def custom(x, z):
    d = {'activity': x.activity, 'application': message_application.mid(x.application),
         'application_id': x.application_id,
         'attachments': [await attachment.mid(y, z, x.id) for y in x.attachments],
         'content': x.content, 'created_at': datetime.mid(x.created_at),
         'edited_at': datetime.mid(x.edited_at), 'embeds': [embed.mid(y) for y in x.embeds],
         'flags': message_flags.low(x.flags), 'id': x.id,
         'interaction': message_interaction.mid(x.interaction), 'jump_url': x.jump_url,
         'mention_everyone': x.mention_everyone, 'mentions': [abc_user.low(y) for y in x.mentions], 'nonce': x.nonce,
         'pinned': x.pinned, 'position': x.position, 'raw_channel_mentions': x.raw_channel_mentions,
         'raw_mentions': x.raw_mentions, 'raw_role_mentions': x.raw_role_mentions,
         'reactions': [reaction.mid(y) for y in x.reactions], 'role_mentions': [role.low(y) for y in x.role_mentions],
         'role_subscription': role_subscription_info.mid(x.role_subscription),
         'stickers': [sticker_item.mid(y) for y in x.stickers], 'system_content': x.system_content, 'tts': x.tts,
         'type': message_type.mid(x.type), 'webhook_id': x.webhook_id}
    try:
        d['author'] = member.low(x.author)
    except AttributeError:
        d['author'] = abc_user.low(x.author)
    d['channel_mentions'] = []
    for channel_mention in x.channel_mentions:
        try:
            d['channel_mentions'].append(thread.low(channel_mention))
        except Exception:
            d['channel_mentions'].append(abc_guild_channel.low(channel_mention))
    d['components'] = []
    for component in x.components:
        if str(component.type) == 'ComponentType.action_row':
            d['components'].append(action_row.low())
        elif str(component.type) == 'ComponentType.button':
            d['components'].append(button.low(component))
        else:
            d['components'].append(select_menu.low(component))
    return d


async def high(x, z):
    d = {'activity': x.activity, 'application': message_application.mid(x.application),
         'application_id': x.application_id,
         'attachments': [await attachment.mid(y, z, x.id) for y in x.attachments],
         'clean_content': x.clean_content, 'content': x.content, 'created_at': datetime.mid(x.created_at),
         'edited_at': datetime.mid(x.edited_at), 'embeds': [embed.mid(y) for y in x.embeds],
         'flags': message_flags.mid(x.flags), 'guild': guild.mid(x.guild), 'id': x.id,
         'interaction': message_interaction.mid(x.interaction), 'jump_url': x.jump_url,
         'mention_everyone': x.mention_everyone, 'mentions': [abc_user.mid(y) for y in x.mentions], 'nonce': x.nonce,
         'pinned': x.pinned, 'position': x.position, 'raw_channel_mentions': x.raw_channel_mentions,
         'raw_mentions': x.raw_mentions, 'raw_role_mentions': x.raw_role_mentions,
         'reactions': [reaction.mid(y) for y in x.reactions], 'role_mentions': [role.mid(y) for y in x.role_mentions],
         'role_subscription': role_subscription_info.mid(x.role_subscription),
         'stickers': [sticker_item.mid(y) for y in x.stickers], 'system_content': x.system_content, 'tts': x.tts,
         'type': message_type.mid(x.type), 'webhook_id': x.webhook_id}
    try:
        d['author'] = member.mid(x.author)
    except AttributeError:
        d['author'] = abc_user.mid(x.author)
    if str(x.channel.type) == 'text':
        d['channel'] = text_channel.mid(x.channel)
    elif str(x.channel.type) in ['public_thread', 'private_thread', 'news_thread']:
        d['channel'] = thread.mid(x.channel)
    elif str(x.channel.type) == 'voice':
        d['channel'] = voice_channel.mid(x.channel)
    elif str(x.channel.type) == 'private':
        d['channel'] = dm_channel.mid(x.channel)
    elif str(x.channel.type) == 'group':
        d['channel'] = group_channel.mid(x.channel)
    elif str(x.channel.type) == 'stage':
        d['channel'] = stage_channel.mid(x.channel)
    else:
        d['channel'] = partial_messageable.mid(x.channel)
    d['channel_mentions'] = []
    for channel_mention in x.channel_mentions:
        try:
            d['channel_mentions'].append(thread.mid(channel_mention))
        except Exception:
            d['channel_mentions'].append(abc_guild_channel.mid(channel_mention))
    d['components'] = []
    for component in x.components:
        if str(component.type) == 'action_row':
            d['components'].append(action_row.mid(component))
        elif str(component.type) == 'button':
            d['components'].append(button.mid(component))
        else:
            d['components'].append(select_menu.mid(component))
    return d


def mid(x):
    d = {'activity': x.activity, 'application': message_application.low(x.application),
         'application_id': x.application_id,
         'attachments': [attachment.low(y) for y in x.attachments],
         'clean_content': x.clean_content, 'content': x.content, 'created_at': datetime.low(x.created_at),
         'edited_at': datetime.low(x.edited_at), 'embeds': [embed.low(y) for y in x.embeds],
         'flags': message_flags.low(x.flags), 'guild': guild.low(x.guild), 'id': x.id,
         'interaction': message_interaction.low(x.interaction), 'jump_url': x.jump_url,
         'mention_everyone': x.mention_everyone, 'mentions': [abc_user.low(y) for y in x.mentions], 'nonce': x.nonce,
         'pinned': x.pinned, 'position': x.position, 'raw_channel_mentions': x.raw_channel_mentions,
         'raw_mentions': x.raw_mentions, 'raw_role_mentions': x.raw_role_mentions,
         'reactions': [reaction.low(y) for y in x.reactions], 'role_mentions': [role.low(y) for y in x.role_mentions],
         'role_subscription': role_subscription_info.low(x.role_subscription),
         'stickers': [sticker_item.low(y) for y in x.stickers], 'system_content': x.system_content, 'tts': x.tts,
         'type': message_type.low(x.type), 'webhook_id': x.webhook_id}
    try:
        d['author'] = member.low(x.author)
    except AttributeError:
        d['author'] = abc_user.low(x.author)
    if str(x.channel.type) == 'text':
        d['channel'] = text_channel.low(x.channel)
    elif str(x.channel.type) in ['public_thread', 'private_thread', 'news_thread']:
        d['channel'] = thread.low(x.channel)
    elif str(x.channel.type) == 'voice':
        d['channel'] = voice_channel.low(x.channel)
    elif str(x.channel.type) == 'private':
        d['channel'] = dm_channel.low(x.channel)
    elif str(x.channel.type) == 'group':
        d['channel'] = group_channel.low(x.channel)
    elif str(x.channel.type) == 'stage':
        d['channel'] = stage_channel.low(x.channel)
    else:
        d['channel'] = partial_messageable.low(x.channel)
    d['channel_mentions'] = []
    for channel_mention in x.channel_mentions:
        try:
            d['channel_mentions'].append(thread.low(channel_mention))
        except Exception:
            d['channel_mentions'].append(abc_guild_channel.low(channel_mention))
    d['components'] = []
    for component in x.components:
        if str(component.type) == 'action_row':
            d['components'].append(action_row.low())
        elif str(component.type) == 'button':
            d['components'].append(button.low(component))
        else:
            d['components'].append(select_menu.low(component))
    return d


def low(x):
    return {'activity': x.activity, 'application_id': x.application_id, 'clean_content': x.clean_content,
            'content': x.content, 'id': x.id, 'jump_url': x.jump_url, 'mention_everyone': x.mention_everyone,
            'nonce': x.nonce, 'pinned': x.pinned, 'position': x.position,
            'raw_channel_mentions': x.raw_channel_mentions, 'raw_mentions': x.raw_mentions,
            'raw_role_mentions': x.raw_role_mentions, 'system_content': x.system_content, 'tts': x.tts,
            'webhook_id': x.webhook_id}
