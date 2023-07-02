from models import asset, base_activity, color, datetime, dm_channel, guild, member_flags, permissions, \
    public_user_flags, role, spotify, status, voice_state


async def high(x):
    d = {'accent_color': color.mid(x.accent_color), 'accent_colour': color.mid(x.accent_colour),
         'avatar': await asset.mid(x.avatar, f'member__avatar__{x.id}'),
         'banner': await asset.mid(x.banner, f'member__banner__{x.id}'), 'bot': x.bot, 'color': color.mid(x.color),
         'colour': color.mid(x.colour), 'created_at': datetime.mid(x.created_at),
         'default_avatar': await asset.mid(x.default_avatar, f'member__default_avatar__{x.id}'),
         'desktop_status': status.mid(x.desktop_status), 'discriminator': x.discriminator,
         'display_avatar': await asset.mid(x.display_avatar, f'member__display_avatar__{x.id}'),
         'display_icon': await asset.mid(x.display_icon, f'member__display_icon__{x.id}'),
         'display_name': x.display_name, 'dm_channel': dm_channel.mid(x.dm_channel), 'flags': member_flags.mid(x.flags),
         'global_name': x.global_name, 'guild': guild.mid(x.guild),
         'guild_avatar': await asset.mid(x.guild_avatar, f'member__guild_avatar__{x.id}'),
         'guild_permissions': permissions.mid(x.guild_permissions), 'id': x.id, 'joined_at': datetime.mid(x.joined_at),
         'mention': x.mention, 'mobile_status': status.mid(x.mobile_status),
         'mutual_guilds': [guild.mid(y) for y in x.mutual_guilds], 'name': x.name, 'nick': x.nick, 'pending': x.pending,
         'premium_since': datetime.mid(x.premium_since), 'public_flags': public_user_flags.mid(x.public_flags),
         'raw_status': x.raw_status, 'resolved_permissions': permissions.mid(x.resolved_permissions),
         'roles': [role.mid(y) for y in x.roles], 'status': status.mid(x.status), 'system': x.system,
         'timed_out_until': datetime.mid(x.timed_out_until), 'top_role': role.mid(x.top_role),
         'voice': voice_state.mid(x.voice), 'web_status': status.mid(x.web_status), 'activities': []}
    for y in x.activities:
        try:
            d['activities'].append(base_activity.mid(y))
        except Exception:
            d['activities'].append(spotify.mid(y))
    try:
        d['activity'].append(base_activity.mid(x.activity))
    except Exception:
        d['activity'].append(spotify.mid(x.activity))
    return d


def mid(x):
    d = {'accent_color': color.low(x.accent_color), 'accent_colour': color.low(x.accent_colour),
         'avatar': asset.low(x.avatar), 'banner': asset.low(x.banner), 'bot': x.bot, 'color': color.low(x.color),
         'colour': color.low(x.colour), 'created_at': datetime.low(x.created_at),
         'default_avatar': asset.low(x.default_avatar), 'desktop_status': status.low(x.desktop_status),
         'discriminator': x.discriminator, 'display_avatar': asset.low(x.display_avatar),
         'display_icon': asset.low(x.display_icon), 'display_name': x.display_name,
         'dm_channel': dm_channel.low(x.dm_channel), 'flags': member_flags.low(x.flags), 'global_name': x.global_name,
         'guild': guild.low(x.guild), 'guild_avatar': asset.low(x.guild_avatar),
         'guild_permissions': permissions.low(x.guild_permissions), 'id': x.id, 'joined_at': datetime.low(x.joined_at),
         'mention': x.mention, 'mobile_status': status.low(x.mobile_status),
         'mutual_guilds': [guild.low(y) for y in x.mutual_guilds], 'name': x.name, 'nick': x.nick, 'pending': x.pending,
         'premium_since': datetime.low(x.premium_since), 'public_flags': public_user_flags.low(x.public_flags),
         'raw_status': x.raw_status, 'resolved_permissions': permissions.low(x.resolved_permissions),
         'roles': [role.low(y) for y in x.roles], 'status': status.low(x.status), 'system': x.system,
         'timed_out_until': datetime.low(x.timed_out_until), 'top_role': role.low(x.top_role),
         'voice': voice_state.low(x.voice), 'web_status': status.low(x.web_status), 'activities': []}
    for y in x.activities:
        try:
            d['activities'].append(base_activity.low())
        except Exception:
            d['activities'].append(spotify.low(y))
    try:
        d['activity'].append(base_activity.low())
    except Exception:
        d['activity'].append(spotify.low(x.activity))
    return d


def low(x):
    return {'bot': x.bot, 'discriminator': x.discriminator, 'display_name': x.display_name,
            'global_name': x.global_name, 'id': x.id, 'mention': x.mention, 'name': x.name, 'nick': x.nick,
            'pending': x.pending, 'raw_status': x.raw_status, 'system': x.system}
