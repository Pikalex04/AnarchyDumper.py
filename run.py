from discord import Client
from SETTINGS import TOKEN, BOT, CHANNELS
from json import dump
from time import time
from os import mkdir, getcwd

client = Client()
x = 0
b = 0


def json_dump(n, d):
    with open(n, 'w+') as f:
        dump(d, f)
        f.close()


def make_dir(d):
    try:
        mkdir(d)
    except FileExistsError:
        return


def dump_datetime(d):
    try:
        return {'year': d.year, 'month': d.month, 'day': d.day, 'hour': d.hour, 'minute': d.minute, 'second': d.second,
                'microsecond': d.microsecond, 'tzinfo': d.tzinfo, 'fold': d.fold}
    except AttributeError:
        return {}


def dump_timedelta(t):
    return {'days': t.days, 'seconds': t.seconds, 'milliseconds': t.milliseconds, 'minutes': t.minutes,
            'hours': t.hours, 'weeks': t.weeks}


def dump_abc_user(u):
    return {'name': u.name, 'discriminator': u.discriminator, 'avatar': u.avatar, 'bot': u.bot,
            'display_name': u.display_name, 'mention': u.mention}


def dump_abc_guild_channel(c):
    return {'name': c.name, 'guild': soft_dump_guild(c.guild), 'position': c.position,
            'changed_roles': [].extend(soft_dump_role(changed_role) for changed_role in c.changed_roles),
            'mention': c.mention, 'created_at': dump_datetime(c.created_at),
            'category': soft_dump_category_channel(c.category), 'permissions_synced': c.permissions_synced}


def soft_dump_abc_guild_channel(c):
    return {'name': c.name, 'position': c.position, 'mention': c.mention, 'permissions_synced': c.permissions_synced}


def soft_dump_user(u):
    return {'name': u.name, 'id': u.id, 'discriminator': u.discriminator, 'avatar': u.avatar, 'bot': u.bot,
            'system': u.system, 'is_friend()': u.is_friend(), 'is_blocked()': u.is_blocked(),
            'default_avatar': str(u.default_avatar), 'display_name': u.display_name,
            'is_avatar_animated()': u.is_avatar_animated(), 'mention': u.mention}


async def dump_attachment(a, c):
    global b
    await a.save(f'dumps/{c}/attachments/{b}_{a.filename}')
    d = {'id': a.id, 'size': a.size, 'height': a.height, 'width': a.width, 'filename': a.filename, 'url': a.url,
         'proxy_url': a.proxy_url, 'is_spoiler()': a.is_spoiler(), 'download_id': b}
    b += 1
    return d


async def dump_asset(a, c):
    global x
    try:
        await a.save(f'dumps/{c}/assets/{x}')
        x += 1
    except Exception:
        pass
    return {}


def soft_dump_message(m):
    return {'tts': m.tts, 'type': str(m.type), 'content': m.content, 'mention_everyone': m.mention_everyone, 'id': m.id,
            'webhook_id': m.webhook_id, 'pinned': m.pinned, 'activity': m.activity, 'application': m.application,
            'raw_mentions': m.raw_mentions, 'raw_channel_mentions': m.raw_channel_mentions,
            'raw_role_mentions': m.raw_role_mentions, 'clean_content': m.clean_content, 'jump_url': m.jump_url,
            'is_system()': m.is_system(), 'system_content': m.system_content}


def dump_reaction(r):
    return {'emoji': {**soft_dump_emoji(r.emoji), **soft_dump_partial_emoji(r.emoji)}, 'count': r.count, 'me': r.me,
            'message': soft_dump_message(r.message), 'custom_emoji': r.custom_emoji}


def dump_call_message(m):
    return {'ended_timestamp': dump_datetime(m.ended_timestamp),
            'partecipants': [].extend(soft_dump_user(partecipant) for partecipant in m.partecipants),
            'call_ended': m.call_ended, 'message': soft_dump_message(m.message),
            'channel': soft_dump_group_channel(m.channel), 'duration': dump_timedelta(m.duration)}


async def dump_guild(g, c):
    return {'name': g.name, 'emojis': [].extend(soft_dump_emoji(emoji) for emoji in g.emojis), 'region': str(g.region),
            'afk_timeout': g.afk_timeout, 'afk_channel': soft_dump_voice_channel(g.afk_channel), 'icon': g.icon,
            'id': g.id, 'owner_id': g.owner_id,
            'unavailable': g.unavailable, 'max_presences': g.max_presences, 'max_members': g.max_members,
            'max_video_channel_users': g.max_video_channel_users, 'banner': g.banner, 'description': g.description,
            'mfa_level': g.mfa_level, 'verification_level': str(g.verification_level),
            'explicit_content_filter': str(g.explicit_content_filter),
            'default_notifications': str(g.default_notifications), 'features': g.features, 'splash': g.splash,
            'premium_tier': g.premium_tier, 'premium_subscription_count': g.premium_subscription_count,
            'preferred_locale': g.preferred_locale, 'discovery_splash': g.discovery_splash, 'large': g.large,
            'me': soft_dump_member(g.me), 'voice_client': str(g.voice_client),
            'channels': [].extend(soft_dump_abc_guild_channel(channel) for channel in g.channels),
            'text_channels': [].extend(soft_dump_text_channel(text_channel) for text_channel in g.text_channels),
            'voice_channels': [].extend(soft_dump_voice_channel(voice_channel) for voice_channel in g.voice_channels),
            'categories': [].extend(soft_dump_category_channel(category) for category in g.categories),
            'system_channel': soft_dump_text_channel(g.system_channel),
            'system_channel_flags': dump_system_channel_flags(g.system_channel_flags),
            'rules_channel': soft_dump_text_channel(g.rules_channel),
            'public_updates_channel': soft_dump_text_channel(g.public_updates_channel), 'emoji_limit': g.emoji_limit,
            'bitrate_limit': g.bitrate_limit, 'filesize_limit': g.filesize_limit,
            'members': [].extend(soft_dump_member(member) for member in g.members),
            'premium_subscribers': [].extend(soft_dump_member(member) for member in g.premium_subscribers),
            'roles': [].extend(soft_dump_role(role) for role in g.roles),
            'default_role': soft_dump_role(g.default_role), 'owner': soft_dump_member(g.owner),
            'icon_url': await dump_asset(g.icon_url, c), 'banner_url': await dump_asset(g.banner_url, c),
            'splash_url': await dump_asset(g.splash_url, c),
            'discovery_splash_url': await dump_asset(g.discovery_splash_url, c),
            'is_icon_animated()': g.is_icon_animated(), 'member_count': g.member_count, 'chunked': g.chunked,
            'shard_id': g.shard_id, 'created_at': dump_datetime(g.created_at)}


def soft_dump_guild(g):
    return {'name': g.name, 'region': str(g.region), 'afk_timeout': g.afk_timeout, 'icon': g.icon, 'id': g.id,
            'owner_id': g.owner_id, 'unavailable': g.unavailable, 'max_presences': g.max_presences,
            'max_members': g.max_members, 'max_video_channel_users': g.max_video_channel_users, 'banner': g.banner,
            'description': g.description, 'mfa_level': g.mfa_level, 'verification_level': str(g.verification_level),
            'explicit_content_filter': str(g.explicit_content_filter),
            'default_notifications': str(g.default_notifications), 'features': g.features, 'splash': g.splash,
            'premium_tier': g.premium_tier, 'premium_subscription_count': g.premium_subscription_count,
            'preferred_locale': g.preferred_locale, 'discovery_splash': g.discovery_splash, 'large': g.large,
            'emoji_limit': g.emoji_limit, 'bitrate_limit': g.bitrate_limit, 'filesize_limit': g.filesize_limit,
            'is_icon_animated()': g.is_icon_animated(), 'member_count': g.member_count, 'chunked': g.chunked,
            'shard_id': g.shard_id}


def soft_dump_member(m):
    try:
        r = {'nick': m.nick, 'raw_status': m.raw_status, 'status': str(m.status), 'mobile_status': str(m.mobile_status),
             'desktop_status': str(m.desktop_status), 'web_status': str(m.web_status),
             'is_on_mobile()': m.is_on_mobile(), 'mention': m.mention, 'display_name': m.display_name,
             'avatar': m.avatar, 'bot': m.bot, 'default_avatar': str(m.default_avatar),
             'discriminator': m.discriminator,
             'id': m.id, 'is_avatar_animated': m.is_avatar_animated(), 'name': m.name, 'system': m.system}
        try:
            r['is_blocked()'] = m.is_blocked()
        except AttributeError:
            pass
        try:
            r['is_friend()'] = m.is_friend()
        except AttributeError:
            pass
        return r
    except AttributeError:
        return {}


def soft_dump_emoji(e):
    try:
        return {'name': e.name, 'id': e.id, 'require_colons': e.require_colons, 'animated': e.animated,
                'managed': e.managed, 'guild_id': e.guild_id, 'available': e.available, 'is_usable()': e.is_usable()}
    except AttributeError:
        return {'raw': e}


def soft_dump_partial_emoji(e):
    try:
        return {'name': e.name, 'animated': e.animated, 'id': e.id, 'is_custom_emoji()': e.is_custom_emoji(),
                'is_unicode_emoji()': e.is_unicode_emoji()}
    except AttributeError:
        return {'raw': e}


def dump_role(r):
    return {'id': r.id, 'name': r.name, 'guild': soft_dump_guild(r.guild), 'hoist': r.hoist, 'position': r.position,
            'managed': r.managed, 'mentionable': r.mentionable, 'is_default()': r.is_default(),
            'permissions': dump_permissions(r.permissions), 'color': dump_color(r.color),
            'created_at': dump_datetime(r.created_at), 'mention': r.mention,
            'members': [].extend(soft_dump_member(member) for member in r.members)}


def soft_dump_role(r):
    return {'id': r.id, 'name': r.name, 'hoist': r.hoist, 'position': r.position, 'managed': r.managed,
            'mentionable': r.mentionable, 'is_default()': r.is_default(), 'mention': r.mention}


def soft_dump_text_channel(c):
    try:
        return {'name': c.name, 'id': c.id, 'category_id': c.category_id, 'topic': c.topic, 'position': c.position,
                'last_message_id': c.last_message_id, 'slowmode_delay': c.slowmode_delay, 'type': str(c.type),
                'is_nsfw()': c.is_nsfw(), 'is_news()': c.is_news(), 'mention': c.mention,
                'permissions_synced': c.permissions_synced}
    except AttributeError:
        return {}


def soft_dump_voice_channel(c):
    try:
        return {'name': c.name, 'id': c.id, 'category_id': c.category_id, 'position': c.position, 'bitrate': c.bitrate,
                'user_limit': c.user_limit, 'type': str(c.type), 'mention': c.mention,
                'permissions_synced': c.permissions_synced}
    except AttributeError:
        return {}


def soft_dump_category_channel(c):
    return {'name': c.name, 'id': c.id, 'position': c.position, 'type': str(c.type), 'is_nsfw()': c.is_nsfw(),
            'mention': c.mention, 'permissions_synced': c.permissions_synced}


def soft_dump_group_channel(c):
    return {'id': c.id, 'icon': c.icon, 'name': c.name, 'type': str(c.type)}


def dump_message_reference(r):
    return {'message_id': r.message_id, 'channel_id': r.channel_id, 'guild': r.guild_id,
            'cached_message': soft_dump_message(r.cached_message)}


def dump_embed(e):
    return {'title': str(e.title), 'type': str(e.type), 'description': str(e.description), 'url': str(e.url),
            'timestamp': dump_datetime(e.timestamp), 'color': dump_color(e.color), 'footer': str(e.footer),
            'image': str(e.image), 'thumbnail': str(e.thumbnail), 'video': str(e.video), 'provider': str(e.provider),
            'author': str(e.author), 'fields': [].extend(str(field) for field in e.fields)}


def dump_color(c):
    try:
        return {'value': c.value, 'r': c.r, 'g': c.g, 'b': c.b}
    except AttributeError:
        return {'raw': c}


def dump_permissions(p):
    return {'value': p.value, 'create_instant_invite': p.create_instant_invite, 'kick_members': p.kick_members,
            'ban_members': p.ban_members, 'administrator': p.administrator, 'manage_channels': p.manage_channels,
            'manage_guild': p.manage_guild, 'add_reactions': p.add_reactions, 'view_audit_log': p.view_audit_log,
            'priority_speaker': p.priority_speaker, 'stream': p.stream, 'read_messages': p.read_messages,
            'view_channel': p.view_channel, 'send_messages': p.send_messages, 'send_tts_messages': p.send_tts_messages,
            'manage_messages': p.manage_messages, 'embed_links': p.embed_links, 'attach_files': p.attach_files,
            'read_message_history': p.read_message_history, 'mention_everyone': p.mention_everyone,
            'external_emojis': p.external_emojis, 'view_guild_insights': p.view_guild_insights, 'connect': p.connect,
            'speak': p.speak, 'mute_members': p.mute_members, 'deafen_members': p.deafen_members,
            'move_members': p.move_members, 'use_voice_activation': p.use_voice_activation,
            'change_nickname': p.change_nickname, 'manage_nicknames': p.manage_nicknames,
            'manage_roles': p.manage_roles, 'manage_webhooks': p.manage_webhooks, 'manage_emojis': p.manage_emojis}


def dump_message_flags(f):
    o = {'value': f.value, 'crossposted': f.crossposted, 'suppress_embeds': f.suppress_embeds, 'urgent': f.urgent}
    try:
        o['is_crossposted()'] = f.is_crossposted()
    except TypeError:
        pass
    try:
        o['source_message_delete'] = f.source_message_delete
    except AttributeError:
        pass
    return o


def dump_system_channel_flags(f):
    return {'value': f.value, 'join_notifications': f.join_notifications,
            'premium_subscriptions': f.premium_subscriptions}


async def start():
    x = time()
    for c in CHANNELS:
        c = client.get_channel(c)
        i = c.id
        w = getcwd()
        s = f'{w}/dumps/{i}'
        for r in [s, f'{s}/attachments', f'{s}/assets']:
            make_dir(r)
        d = {}
        n = 0
        json_dump(f'dumps/{c.id}/guild.json', await dump_guild(c.guild, i))
        async for m in c.history(limit=None, oldest_first=True):
            d[n] = {}
            d[n]['tts'] = m.tts
            d[n]['type'] = m.type
            d[n]['author'] = dump_abc_user(m.author)
            d[n]['content'] = m.content
            d[n]['embeds'] = [].extend(dump_embed(embed) for embed in m.embeds)
            try:
                d[n]['call'] = dump_call_message(m.call)
            except AttributeError:
                pass
            try:
                d[n]['reference'] = dump_message_reference(m.reference)
            except AttributeError:
                pass
            d[n]['mention_everyone'] = m.mention_everyone
            d[n]['mentions'] = [].extend(dump_abc_user(mention) for mention in m.mentions)
            d[n]['channel_mentions'] = [].extend(dump_abc_guild_channel(channel_mention)
                                                 for channel_mention in m.channel_mentions)
            d[n]['role_mentions'] = [].extend(dump_role(role_mention) for role_mention in m.role_mentions)
            d[n]['id'] = m.id
            d[n]['webhook_id'] = m.webhook_id
            d[n]['attachments'] = []
            for attachment in m.attachments:
                d[n]['attachments'].append(await dump_attachment(attachment, i))
            d[n]['pinned'] = m.pinned
            d[n]['flags'] = dump_message_flags(m.flags)
            d[n]['reactions'] = [].extend(dump_reaction(reaction) for reaction in m.reactions)
            d[n]['activity'] = m.activity
            d[n]['application'] = m.application
            d[n]['raw_mentions'] = m.raw_mentions
            d[n]['raw_channel_mentions'] = m.raw_channel_mentions
            d[n]['raw_role_mentions'] = m.raw_role_mentions
            d[n]['clean_content'] = m.clean_content
            d[n]['created_at'] = dump_datetime(m.created_at)
            d[n]['edited_at'] = dump_datetime(m.edited_at)
            d[n]['jump_url'] = m.jump_url
            d[n]['is_system()'] = m.is_system()
            d[n]['system_content'] = m.system_content
            print(f'Message {n} got dumped successfully.')
            n += 1
        json_dump(f'dumps/{c.id}/messages.json', d)
        print(f'{c.name} dumped successfully.')
    print(f'Operation completed successfully in {time() - x}')


@client.event
async def on_ready():
    await start()
    exit()


client.run(TOKEN, bot=BOT)
