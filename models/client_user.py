from models import asset, color, datetime, guild, public_user_flags


async def high(x):
    return {'accent_color': color.mid(x.accent_color), 'accent_colour': color.mid(x.accent_colour),
            'avatar': await asset.mid(x.avatar, f'member__avatar__{x.id}'),
            'banner': await asset.mid(x.banner, f'member__banner__{x.id}'), 'bot': x.bot, 'color': color.mid(x.color),
            'colour': color.mid(x.colour), 'created_at': datetime.mid(x.created_at),
            'default_avatar': await asset.mid(x.default_avatar, f'member__default_avatar__{x.id}'),
            'discriminator': x.discriminator,
            'display_avatar': await asset.mid(x.display_avatar, f'member__display_avatar__{x.id}'),
            'display_name': x.display_name, 'global_name': x.global_name, 'id': x.id, 'locale': x.locale,
            'mention': x.mention, 'mfa_enabled': x.mfa_enabled,
            'mutual_guilds': [guild.mid(y) for y in x.mutual_guilds], 'name': x.name,
            'public_flags': public_user_flags.mid(x.public_flags), 'system': x.system, 'verified': x.verified}


def mid(x):
    return {'accent_color': color.low(x.accent_color), 'accent_colour': color.low(x.accent_colour),
            'avatar': asset.low(x.avatar), 'banner': asset.low(x.banner), 'bot': x.bot, 'color': color.low(x.color),
            'colour': color.low(x.colour), 'created_at': datetime.low(x.created_at),
            'default_avatar': asset.low(x.default_avatar), 'discriminator': x.discriminator,
            'display_avatar': asset.low(x.display_avatar), 'display_name': x.display_name, 'global_name': x.global_name,
            'id': x.id, 'locale': x.locale, 'mention': x.mention, 'mfa_enabled': x.mfa_enabled,
            'mutual_guilds': [guild.low(y) for y in x.mutual_guilds], 'name': x.name,
            'public_flags': public_user_flags.low(x.public_flags), 'system': x.system, 'verified': x.verified}


def low(x):
    return {'bot': x.bot, 'discriminator': x.discriminator, 'display_name': x.display_name,
            'global_name': x.global_name, 'id': x.id, 'locale': x.locale, 'mention': x.mention,
            'mfa_enabled': x.mfa_enabled, 'name': x.name, 'system': x.system, 'verified': x.verified}
