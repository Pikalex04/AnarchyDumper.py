from models import abc_guild_channel, asset, category_channel, content_filter, datetime, emoji, forum_channel, \
    guild_sticker, locale, member, mfa_level, notification_level, nsfw_level, role, scheduled_event, stage_channel, \
    stage_instance, system_channel_flags, text_channel, thread, verification_level, voice_channel


async def high(x):
    d = {'afk_channel': voice_channel.mid(x.afk_channel) if str(x.afk_channel.type) == 'voice' else
         stage_channel.mid(x.afk_channel), 'afk_timeout': x.afk_timeout,
         'approximate_member_count': x.approximate_member_count,
         'approximate_presence_count': x.approximate_presence_count,
         'banner': await asset.mid(x.banner, f'guild__banner__{x.id}'), 'bitrate_limit': x.bitrate_limit,
         'categories': [category_channel.mid(y) for y in x.categories],
         'channels': [abc_guild_channel.mid(y) for y in x.channels], 'chunked': x.chunked,
         'created_at': datetime.mid(x.created_at),
         'default_notifications': notification_level.mid(x.default_notifications),
         'default_role': role.mid(x.default_role), 'description': x.description,
         'discovery_splash': await asset.mid(x.discovery_splash, f'guild__discovery_splash__{x.id}'),
         'emoji_limit': x.emoji_limit, 'emojis': [emoji.mid(y) for y in x.emojis],
         'explicit_content_filter': content_filter.mid(x.explicit_content_filter), 'features': x.features,
         'filesize_limit': x.filesize_limit, 'forums': [forum_channel.mid(y) for y in x.forums],
         'icon': await asset.mid(x.icon, f'guild__icon__{x.id}'), 'id': x.id, 'large': x.large,
         'max_members': x.max_members, 'max_presences': x.max_presences,
         'max_stage_video_users': x.max_stage_video_users, 'max_video_channel_users': x.max_video_channel_users,
         'me': member.mid(x.me), 'member_count': x.member_count, 'members': [member.mid(y) for y in x.members],
         'mfa_level': mfa_level.mid(x.mfa_level), 'name': x.name, 'nsfw_level': nsfw_level.mid(x.nsfw_level),
         'owner': member.mid(x.owner), 'owner_id': x.owner_id, 'preferred_locale': locale.mid(x.preferred_locale),
         'premium_progress_bar_enabled': x.premium_progress_bar_enabled,
         'premium_subscriber_role': role.mid(x.premium_subscriber_role),
         'premium_subscribers': [member.mid(y) for y in x.premium_subscribers],
         'premium_subscription_count': x.premium_subscription_count, 'premium_tier': x.premium_tier,
         'public_updates_channel': text_channel.mid(x.public_updates_channel), 'roles': [role.mid(y) for y in x.roles],
         'rules_channel': text_channel.mid(x.rules_channel),
         'safety_alerts_channel': text_channel.mid(x.safety_alerts_channel),
         'scheduled_events': [scheduled_event.mid(y) for y in x.scheduled_events], 'self_role': role.mid(x.self_role),
         'shard_id': x.shard_id, 'splash': await asset.mid(x.splash, f'guild__splash__{x.id}'),
         'stage_channels': [stage_channel.mid(y) for y in x.stage_channels],
         'stage_instances': [stage_instance.mid(y) for y in x.stage_instances], 'sticker_limit': x.sticker_limit,
         'stickers': [guild_sticker.mid(y) for y in x.stickers], 'system_channel': text_channel.mid(x.system_channel),
         'system_channel_flags': system_channel_flags.mid(x.system_channel_flags),
         'text_channels': [text_channel.mid(y) for y in x.text_channels], 'threads': [thread.mid(y) for y in x.threads],
         'unavailable': x.unavailable, 'vanity_url': x.vanity_url, 'vanity_url_code': x.vanity_url_code,
         'verification_level': verification_level.mid(x.verification_level),
         'voice_channels': [voice_channel.mid(y) for y in x.voice_channels], 'voice_client': str(x.voice_client),
         'widget_enabled': x.widget_enabled}
    try:
        if str(x.widget_channel.type) == 'text':
            d['widget_channel'] = text_channel.mid(x.widget_channel)
        elif str(x.widget_channel.type) == 'forum':
            d['widget_channel'] = forum_channel.mid(x.widget_channel)
        elif str(x.widget_channel.type) == 'voice':
            d['widget_channel'] = voice_channel.mid(x.widget_channel)
        elif str(x.widget_channel.type) == 'stage':
            d['widget_channel'] = stage_channel.mid(x.widget_channel)
    except AttributeError:
        d['widget_channel'] = 'None'
    return d


def mid(x):
    d = {'afk_channel': voice_channel.low(x.afk_channel) if str(x.afk_channel.type) == 'voice' else
         stage_channel.low(x.afk_channel), 'afk_timeout': x.afk_timeout,
         'approximate_member_count': x.approximate_member_count,
         'approximate_presence_count': x.approximate_presence_count, 'banner': asset.low(x.banner),
         'bitrate_limit': x.bitrate_limit, 'categories': [category_channel.low(y) for y in x.categories],
         'channels': [abc_guild_channel.low(y) for y in x.channels], 'chunked': x.chunked,
         'created_at': datetime.low(x.created_at),
         'default_notifications': notification_level.low(x.default_notifications),
         'default_role': role.low(x.default_role), 'description': x.description,
         'discovery_splash': asset.low(x.discovery_splash), 'emoji_limit': x.emoji_limit,
         'emojis': [emoji.low(y) for y in x.emojis],
         'explicit_content_filter': content_filter.low(x.explicit_content_filter), 'features': x.features,
         'filesize_limit': x.filesize_limit, 'forums': [forum_channel.low(y) for y in x.forums],
         'icon': asset.low(x.icon), 'id': x.id, 'large': x.large, 'max_members': x.max_members,
         'max_presences': x.max_presences, 'max_stage_video_users': x.max_stage_video_users,
         'max_video_channel_users': x.max_video_channel_users, 'me': member.low(x.me), 'member_count': x.member_count,
         'members': [member.low(y) for y in x.members], 'mfa_level': mfa_level.low(x.mfa_level), 'name': x.name,
         'nsfw_level': nsfw_level.low(x.nsfw_level), 'owner': member.low(x.owner), 'owner_id': x.owner_id,
         'preferred_locale': locale.low(x.preferred_locale),
         'premium_progress_bar_enabled': x.premium_progress_bar_enabled,
         'premium_subscriber_role': role.low(x.premium_subscriber_role),
         'premium_subscribers': [member.low(y) for y in x.premium_subscribers],
         'premium_subscription_count': x.premium_subscription_count, 'premium_tier': x.premium_tier,
         'public_updates_channel': text_channel.low(x.public_updates_channel), 'roles': [role.low(y) for y in x.roles],
         'rules_channel': text_channel.low(x.rules_channel),
         'safety_alerts_channel': text_channel.low(x.safety_alerts_channel),
         'scheduled_events': [scheduled_event.low(y) for y in x.scheduled_events], 'self_role': role.low(x.self_role),
         'shard_id': x.shard_id, 'splash': asset.low(x.splash),
         'stage_channels': [stage_channel.low(y) for y in x.stage_channels],
         'stage_instances': [stage_instance.low(y) for y in x.stage_instances], 'sticker_limit': x.sticker_limit,
         'stickers': [guild_sticker.low(y) for y in x.stickers], 'system_channel': text_channel.low(x.system_channel),
         'system_channel_flags': system_channel_flags.low(x.system_channel_flags),
         'text_channels': [text_channel.low(y) for y in x.text_channels], 'threads': [thread.low(y) for y in x.threads],
         'unavailable': x.unavailable, 'vanity_url': x.vanity_url, 'vanity_url_code': x.vanity_url_code,
         'verification_level': verification_level.low(x.verification_level),
         'voice_channels': [voice_channel.low(y) for y in x.voice_channels], 'voice_client': str(x.voice_client),
         'widget_enabled': x.widget_enabled}
    try:
        if str(x.widget_channel.type) == 'text':
            d['widget_channel'] = text_channel.low(x.widget_channel)
        elif str(x.widget_channel.type) == 'forum':
            d['widget_channel'] = forum_channel.low(x.widget_channel)
        elif str(x.widget_channel.type) == 'voice':
            d['widget_channel'] = voice_channel.low(x.widget_channel)
        elif str(x.widget_channel.type) == 'stage':
            d['widget_channel'] = stage_channel.low(x.widget_channel)
    except AttributeError:
        d['widget_channel'] = 'None'
    return d


async def low(x):
    return {'afk_timeout': x.afk_timeout, 'approximate_member_count': x.approximate_member_count,
            'approximate_presence_count': x.approximate_presence_count, 'bitrate_limit': x.bitrate_limit,
            'chunked': x.chunked, 'description': x.description, 'emoji_limit': x.emoji_limit, 'features': x.features,
            'filesize_limit': x.filesize_limit, 'id': x.id, 'large': x.large, 'max_members': x.max_members,
            'max_presences': x.max_presences, 'max_stage_video_users': x.max_stage_video_users,
            'max_video_channel_users': x.max_video_channel_users, 'member_count': x.member_count, 'name': x.name,
            'owner_id': x.owner_id, 'premium_progress_bar_enabled': x.premium_progress_bar_enabled,
            'premium_subscription_count': x.premium_subscription_count, 'premium_tier': x.premium_tier,
            'shard_id': x.shard_id, 'sticker_limit': x.sticker_limit, 'unavailable': x.unavailable,
            'vanity_url': x.vanity_url, 'vanity_url_code': x.vanity_url_code, 'widget_enabled': x.widget_enabled}
