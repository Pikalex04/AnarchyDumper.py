from discord import Client
from SETTINGS import TOKEN, BOT, CHANNELS
from json import dump
from time import time
from asyncio import sleep
client = Client()
attachment_id = 0
asset_id = 0


def json_dump(n, d):
    with open(n, 'w+') as f:
        dump(d, f)
        f.close()


def get_channel(c):
    return client.get_channel(c)


def dump_datetime(d):
    return {'year': d.year, 'month': d.month, 'day': d.day, 'hour': d.hour, 'minute': d.minute, 'second': d.second,
            'microsecond': d.microsecond, 'tzinfo': d.tzinfo, 'fold': d.fold}


def dump_timedelta(t):
    return {'days': t.days, 'seconds': t.seconds, 'milliseconds': t.milliseconds, 'minutes': t.minutes,
            'hours': t.hours, 'weeks': t.weeks}


def dump_abc_user(u):
    return {'name': u.name, 'discriminator': u.discriminator, 'avatar': u.avatar, 'bot': u.bot,
            'display_name': u.display_name, 'mention': u.mention}


async def dump_abc_guild_channel(c):
    return {'name': c.name, 'guild': await dump_guild(c.guild), 'position': c.position,
            'changed_roles': [].extend(await dump_role(changed_role) for changed_role in c.changed_roles),
            'mention': c.mention, 'created_at': dump_datetime(c.created_at),
            'category': await dump_category_channel(c.category), 'permissions_synced': c.permissions_synced}


def dump_abc_messageable():
    return {}


async def dump_client_user(u):
    return {'name': u.name, 'id': u.id, 'discriminator': u.discriminator, 'avatar': u.avatar, 'bot': u.bot,
            'system': u.system, 'verified': u.verified, 'email': u.email, 'locale': u.locale,
            'mfa_enabled': u.mfa_enabled, 'premium': u.premium, 'premium_type': u.premium_type,
            'relationships': [].extend(await dump_relationship(relationship) for relationship in u.relationships),
            'friends': [].extend(await dump_user(friend) for friend in u.friends),
            'blocked': [].extend(await dump_user(blocked) for blocked in u.blocked),
            'avatar_url': await dump_asset(u.avatar_url), 'color': dump_color(u.color),
            'created_at': dump_datetime(u.created_at), 'default_avatar': u.default_avatar,
            'default_avatar_url': await dump_asset(u.default_avatar_url), 'display_name': u.display_name,
            'is_avatar_animated()': u.is_avatar_animated(), 'mention': u.mention,
            'public_flags': dump_public_flags(u.public_flags)}


async def dump_relationship(r):
    return {'user': await dump_user(r.user), 'relationship_type': str(r.relationship_type)}


async def dump_user(u):
    return {'name': u.name, 'id': u.id, 'discriminator': u.discriminator, 'avatar': u.avatar, 'bot': u.bot,
            'system': u.system, 'dm_channel': await dump_dm_channel(u.dm_channel), 'relationship': await u.relationship,
            'is_friend()': u.is_friend(), 'is_blocked()': u.is_blocked(), 'avatar_url': await dump_asset(u.avatar_url),
            'color': dump_color(u.color), 'created_at': dump_datetime(u.created_at),
            'default_avatar': str(u.default_avatar), 'default_avatar_url': await dump_asset(u.default_avatar_url),
            'display_name': u.display_name, 'is_avatar_animated()': u.is_avatar_animated(), 'mention': u.mention,
            'public_flags': dump_public_flags(u.public_flags)}


async def dump_attachment(a):
    global attachment_id
    e = {'id': a.id, 'size': a.size, 'height': a.height, 'width': a.width, 'filename': a.filename, 'url': a.url,
         'proxy_url': a.proxy_url, 'is_spoiler()': a.is_spoiler(), 'download_id': attachment_id}
    await a.save(f'attachments/{attachment_id}_{a.filename}')
    attachment_id += 1
    return e


async def dump_asset(a):
    global asset_id
    e = {'id': a.id, 'size': a.size, 'height': a.height, 'width': a.width, 'filename': a.filename, 'url': a.url,
         'proxy_url': a.proxy_url, 'is_spoiler()': a.is_spoiler(), 'download_id': asset_id}
    await a.save(f'assets/{asset_id}_{a.filename}')
    asset_id += 1
    return e


async def dump_message(m):
    return {'tts': m.tts, 'type': str(m.type), 'author': dump_abc_user(m.author), 'content': m.content,
            'embeds': [].extend(dump_embed(embed) for embed in m.embeds), 'channel': dump_abc_messageable(),
            'call': await dump_call_message(m.call), 'reference': await dump_message_reference(m.reference),
            'mention_everyone': m.mention_everyone,
            'mentions': [].extend(dump_abc_user(mention) for mention in m.mentions),
            'channel_mentions': [].extend(await dump_abc_guild_channel(channel_mention)
                                          for channel_mention in m.channel_mentions),
            'role_mentions': [].extend(await dump_role(role_mention) for role_mention in m.role_mentions), 'id': m.id,
            'webhook_id': m.webhook_id,
            'attachments': [].extend(await dump_attachment(attachment) for attachment in m.attachments),
            'pinned': m.pinned, 'flags': dump_message_flags(m.flags),
            'reactions': [].extend(await dump_reaction(reaction) for reaction in m.reactions), 'activity': m.activity,
            'application': m.application, 'guild': await dump_guild(m.guild), 'raw_mentions': m.raw_mentions,
            'raw_channel_mentions': m.raw_channel_mentions, 'raw_role_mentions': m.raw_role_mentions,
            'clean_content': m.clean_content, 'created_at': dump_datetime(m.created_at),
            'edited_at': dump_datetime(m.edited_at), 'jump_url': m.jump_url, 'is_system()': m.is_system(),
            'system_content': m.system_content}


async def dump_reaction(r):
    return {'emoji': {**await dump_emoji(r.emoji), **await dump_partial_emoji(r.emoji)}, 'count': r.count, 'me': r.me,
            'message': await dump_message(r.message), 'custom_emoji': r.custom_emoji}


async def dump_call_message(m):
    return {'ended_timestamp': dump_datetime(m.ended_timestamp),
            'partecipants': [].extend(await dump_user(partecipant) for partecipant in m.partecipants),
            'message': await dump_message(m.message), 'call_ended': m.call_ended,
            'channel': await dump_group_channel(m.channel), 'duration': dump_timedelta(m.duration)}


async def dump_guild(g):
    return {'name': g.name, 'emojis': [].extend(await dump_emoji(emoji) for emoji in g.emojis), 'region': str(g.region),
            'afk_timeout': g.afk_timeout, 'afk_channel': await dump_voice_channel(g.afk_channel), 'icon': g.icon,
            'id': g.id, 'owner_id': g.owner_id, 'unavailable': g.unavailable, 'max_presences': g.max_presences,
            'max_members': g.max_members, 'max_video_channel_users': g.max_video_channel_users,
            'banner': g.banner, 'description': g.description, 'mfa_level': g.mfa_level,
            'verification_level': str(g.verification_level), 'explicit_content_filter': str(g.explicit_content_filter),
            'default_notifications': str(g.default_notifications), 'features': g.features, 'splash': g.splash,
            'premium_tier': g.premium_tier, 'premium_subscription_count': g.premium_subscription_count,
            'preferred_locale': g.preferred_locale, 'discovery_splash': g.discovery_splash,
            'channels': [].extend(await dump_abc_guild_channel(channel) for channel in g.channels), 'large': g.large,
            'voice_channels': [].extend(await dump_voice_channel(voice_channel) for voice_channel in g.voice_channels),
            'me': await dump_member(g.me), 'voice_client': str(g.voice_client),
            'text_channels': [].extend(await dump_text_channel(text_channel) for text_channel in g.text_channels),
            'categories': [].extend(await dump_category_channel(category) for category in g.category),
            'system_channel': await dump_text_channel(g.system_channel),
            'system_channel_flags': dump_system_channel_flags(g.system_channel_flags),
            'rules_channel': await dump_text_channel(g.rules_channel),
            'public_updates_channel': await dump_text_channel(g.public_updates_channel), 'emoji_limit': g.emoji_limit,
            'bitrate_limit': g.bitrate_limit, 'filesize_limit': g.filesize_limit,
            'members': [].extend(await dump_member(member) for member in g.members),
            'premium_subscribers': [].extend(await dump_member(member) for member in g.premium_subscribers),
            'roles': [].extend(await dump_role(role) for role in g.roles),
            'default_role': await dump_role(g.default_role), 'owner': await dump_member(g.owner),
            'icon_url': await dump_asset(g.icon_url), 'is_icon_animated()': g.is_icon_animated(),
            'banner_url': await dump_asset(g.banner_url), 'splash_url': await dump_asset(g.splash_url),
            'discovery_splash_url': await dump_asset(g.discovery_splash_url), 'member_count': g.member_count,
            'chunked': g.chunked, 'shard_id': g.shard_id, 'created_at': dump_datetime(g.created_at)}


async def dump_member(m):
    return {'joined_at': dump_datetime(m.joined_at),
            'activities': [].extend({**dump_base_activity(activity),
                                     **dump_spotify(activity)} for activity in m.activities),
            'guild': await dump_guild(m.guild), 'nick': m.nick, 'premium_since': dump_datetime(m.premium_since),
            'raw_status': m.raw_status, 'status': str(m.status), 'mobile_status': str(m.mobile_status),
            'desktop_status': str(m.desktop_status), 'web_status': str(m.web_status),
            'is_on_mobile()': m.is_on_mobile(), 'color': dump_color(m.color),
            'roles': [].extend(await dump_role(role) for role in m.roles), 'mention': m.mention,
            'display_name': m.display_name, 'top_role': await dump_role(m.top_role),
            'guild_permissions': dump_permissions(m.guild_permissions), 'voice': await dump_voice_state(m.voice),
            'avatar': m.avatar, 'avatar_url': await dump_asset(m.avatar_url), 'bot': m.bot,
            'created_at': dump_datetime(m.created_at), 'default_avatar': str(m.default_avatar),
            'default_avatar_url': await dump_asset(m.default_avatar_url), 'discriminator': m.discriminator,
            'dm_channel': await dump_dm_channel(m.dm_channel), 'id': m.id, 'is_avatar_animated': m.is_avatar_animated(),
            'is_blocked()': m.is_blocked(), 'is_friend()': m.is_friend(), 'name': m.name,
            'public_flags': dump_public_flags(m.public_flags),
            'relationship': await dump_relationship(m.relationship), 'system': m.system}


def dump_spotify(s):
    return {'type': str(s.type), 'created_at': dump_datetime(s.created_at), 'color': dump_color(s.color),
            'name': s.name, 'title': s.title, 'artists': s.artists, 'album': s.album,
            'album_cover_url': s.album_cover_url, 'track_id': s.track_id, 'start': dump_datetime(s.start),
            'end': dump_datetime(s.end), 'duration': dump_datetime(s.duration), 'party_id': s.party_id}


async def dump_voice_state(s):
    return {'deaf': s.deaf, 'mute': s.mute, 'self_mute': s.self_mute, 'self_deaf': s.self_deaf,
            'self_stream': s.self_stream, 'self_video': s.self_video, 'afk': s.afk,
            'channel': await dump_voice_channel(s.channel)}


async def dump_emoji(e):
    return {'name': e.name, 'id': e.id, 'require_colons': e.require_colons, 'animated': e.animated,
            'managed': e.managed, 'guild_id': e.guild_id, 'available': e.available, 'user': await dump_user(e.user),
            'created_at': dump_datetime(e.created_at), 'url': await dump_asset(e.url),
            'roles': [].extend(await dump_role(role) for role in e.roles), 'guild': await dump_guild(e.guild),
            'is_usable()': e.is_usable()}


async def dump_partial_emoji(e):
    return {'name': e.name, 'animated': e.animated, 'id': e.id, 'is_custom_emoji()': e.is_custom_emoji(),
            'is_unicode_emoji()': e.is_unicode_emoji(), 'url': await dump_asset(e.url)}


async def dump_role(r):
    return {'id': r.id, 'name': r.name, 'guild': await dump_guild(r.guild), 'hoist': r.hoist, 'position': r.position,
            'managed': r.managed, 'mentionable': r.mentionable, 'is_default()': r.is_default(),
            'permissions': dump_permissions(r.permissions), 'color': dump_color(r.color),
            'created_at': dump_datetime(r.created_at), 'mention': r.mention,
            'members': [].extend(await dump_member(member) for member in r.members)}


async def dump_text_channel(c):
    return {'name': c.name, 'guild': await dump_guild(c.guild), 'id': c.id, 'category_id': c.category_id,
            'topic': c.topic, 'position': c.position, 'last_message_id': c.last_message_id,
            'slowmode_delay': c.slowmode_delay,
            'type': str(c.type), 'members': [].extend(await dump_member(member) for member in c.members),
            'is_nsfw()': c.is_nsfw(), 'is_news()': c.is_news(), 'category': await dump_category_channel(c.category),
            'changed_roles': [].extend(await dump_role(changed_role) for changed_role in c.changed_roles),
            'created_at': dump_datetime(c.created_at), 'mention': c.mention, 'permissions_synced': c.permissions_synced}


async def dump_voice_channel(c):
    return {'name': c.name, 'guild': await dump_guild(c.guild), 'id': c.id, 'category_id': c.category_id,
            'position': c.position, 'bitrate': c.bitrate, 'user_limit': c.user_limit, 'type': str(c.type),
            'members': [].extend(await dump_member(member) for member in c.members),
            'category': await dump_category_channel(c.category),
            'changed_roles': [].extend(await dump_role(changed_role) for changed_role in c.changed_roles),
            'created_at': dump_datetime(c.created_at), 'mention': c.mention, 'permissions_synced': c.permissions_synced,
            }


async def dump_category_channel(c):
    return {'name': c.name, 'guild': await dump_guild(c.guild), 'id': c.id, 'position': c.position, 'type': str(c.type),
            'is_nsfw()': c.is_nsfw(),
            'channels': [].extend(await dump_abc_guild_channel(channel) for channel in c.channels),
            'text_channels': [].extend(await dump_text_channel(text_channel) for text_channel in c.text_channels),
            'voice_channels': [].extend(await dump_voice_channel(voice_channel) for voice_channel in c.voice_channels),
            'category': await dump_category_channel(c.category),
            'changed_roles': [].extend(await dump_role(changed_role) for changed_role in c.changed_roles),
            'created_at': dump_datetime(c.created_at), 'mention': c.mention, 'permissions_synced': c.permissions_synced,
            }


async def dump_dm_channel(c):
    return {'recipient': await dump_user(c.recipient), 'me': await dump_client_user(c.me), 'id': c.id,
            'type': str(c.type), 'created_at': dump_datetime(c.created_at)}


async def dump_group_channel(c):
    return {'recipients': [].extend(await dump_user(user) for user in c.recipients), 'me': await dump_client_user(c.me),
            'id': c.id, 'owner': await dump_user(c.owner), 'icon': c.icon, 'name': c.name, 'type': str(c.type),
            'icon_url': await dump_asset(c.icon_url), 'created_at': dump_datetime(c.created_at)}


async def dump_message_reference(r):
    return {'message_id': r.message_id, 'channel_id': r.channel_id, 'guild': r.guild_id,
            'cached_message': await dump_message(r.cached_message)}


def dump_embed(e):
    return {'title': str(e.title), 'type': str(e.type), 'description': str(e.description), 'url': str(e.url),
            'timestamp': dump_datetime(e.timestamp), 'color': dump_color(e.color), 'footer': str(e.footer),
            'image': str(e.image), 'thumbnail': str(e.thumbnail), 'video': str(e.video), 'provider': str(e.provider),
            'author': str(e.author), 'fields': [].extend(str(field) for field in e.fields)}


def dump_color(c):
    return {'value': c.value, 'r': c.r, 'g': c.g, 'b': c.b}


def dump_base_activity(a):
    return {'created_at': dump_datetime(a.created_at)}


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


def dump_system_channel_flags(f):
    return {'value': f.value, 'join_notifications': f.join_notifications,
            'premium_subscriptions': f.premium_subscriptions}


def dump_message_flags(f):
    return {'value': f.value, 'crossposted': f.crossposted, 'is_crossposted()': f.is_crossposted(),
            'suppress_embeds': f.suppress_embeds, 'source_message_delete': f.source_message_delete,
            'urgent': f.urgent}


def dump_public_flags(f):
    return {'value': f.value, 'staff': f.staff, 'partner': f.partner, 'hypesquad': f.hypesquad,
            'bug_hunter': f.bug_hunter, 'hypesquad_bravery': f.hypesquad_bravery,
            'hypesquad_brilliance': f.hypesquad_brilliance, 'hypesquad_balance': f.hypesquad_balance,
            'early_supporter': f.early_supporter, 'team_user': f.team_user, 'system': f.system,
            'bug_hunter_level_2': f.bug_hunter_level_2, 'verified_bot': f.verified_bot,
            'verified_bot_developer': f.verified_bot_developer,
            'early_verified_bot_developer': f.early_verified_bot_developer}


async def start():
    x = time()
    for c in CHANNELS:
        c = get_channel(c)
        d = {}
        n = 0
        async for m in c.history(limit=None, oldest_first=True):
            d[n] = await dump_message(m)
            print(f'Message {n} got dumped successfully.')
            n += 1
        json_dump(f'channels\\{c.id}.json', d)
        print(f'{c.name} dumped successfully.')
    print(f'Operation completed successfully in {time() - x}')


@client.event
async def on_ready():
    await start()
    await sleep(10)
    exit()


client.run(TOKEN, bot=BOT)
