from models import asset


async def high(x):
    return {'avatar': await asset.mid(x.avatar, f'member__avatar__{x.id}'), 'bot': x.bot,
            'default_avatar': await asset.mid(x.default_avatar, f'member__default_avatar__{x.id}'),
            'discriminator': x.discriminator,
            'display_avatar': await asset.mid(x.display_avatar, f'member__display_avatar__{x.id}'),
            'display_name': x.display_name, 'global_name': x.global_name, 'mention': x.mention, 'name': x.name,
            'system': x.system}


def mid(x):
    return {'avatar': asset.low(x.avatar), 'bot': x.bot, 'default_avatar': asset.low(x.default_avatar),
            'discriminator': x.discriminator, 'display_avatar': asset.low(x.display_avatar),
            'display_name': x.display_name, 'global_name': x.global_name, 'mention': x.mention, 'name': x.name,
            'system': x.system}


def low(x):
    return {'bot': x.bot, 'discriminator': x.discriminator, 'display_name': x.display_name,
            'global_name': x.global_name, 'mention': x.mention, 'name': x.name, 'system': x.system}
