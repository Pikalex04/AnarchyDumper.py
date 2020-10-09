from discord import Client
from SETTINGS import TOKEN, BOT, CHANNELS
from json import dump
from time import time

client = Client()


def json_dump(n, d):
    with open(n, 'w+') as f:
        dump(d, f)
        f.close()


def get_channel(c):
    return client.get_channel(c)


async def dump_channels():
    x = time()
    b = 0
    for c in CHANNELS:
        c = get_channel(c)
        d = {}
        n = 0
        async for m in c.history(limit=None, oldest_first=True):
            d[n] = {}
            d[n]['tts'] = m.tts
            d[n]['type'] = m.type
            d[n]['author'] = {}
            d[n]['author']['name'] = m.author.name
            d[n]['author']['discriminator'] = m.author.discriminator
            d[n]['author']['avatar'] = m.author.avatar
            d[n]['author']['bot'] = m.author.bot
            d[n]['author']['display_name'] = m.author.display_name
            d[n]['author']['mention'] = m.author.mention
            d[n]['content'] = m.content
            d[n]['embeds'] = []
            for e in m.embeds:
                d[n]['embeds'].append({'title': str(e.title), 'type': str(e.type), 'description': str(e.description),
                                       'url': str(e.url),
                                       'timestamp': str(e.timestamp), 'colour': str(e.colour), 'footer': str(e.footer),
                                       'image': str(e.image), 'thumbnail': str(e.thumbnail), 'video': str(e.video),
                                       'provider': str(e.provider), 'author': str(e.author), 'fields': str(e.fields)})
            try:
                d[n]['call'] = m.call
            except Exception:
                pass
            d[n]['reference'] = str(m.reference)
            d[n]['mention_everyone'] = m.mention_everyone
            d[n]['mentions'] = []
            for t in m.mentions:
                d[n]['mentions'].append({'name': t.name, 'discriminator': t.discriminator, 'avatar': t.avatar, 'bot':
                                         t.bot, 'display_name': t.display_name, 'mention': t.mention})
            d[n]['channel_mentions'] = []
            for h in m.channel_mentions:
                d[n]['channel_mentions'].append({'name': h.name, 'guild': str(h.guild), 'position': h.position,
                                                 'changed_roles': str(h.changed_roles), 'mention': h.mention,
                                                 'created_at': str(h.created_at), 'category': h.category,
                                                 'permissions_synced': h.permissions_synced})
            d[n]['role_mentions'] = []
            for r in m.role_mentions:
                d[n]['role_mentions'].append({'id': r.id, 'name': r.name, 'guild': str(r.guild), 'hoist': r.hoist,
                                              'position': r.position, 'managed': r.managed,
                                              'mentionable': r.mentionable, 'is_default()': r.is_default(),
                                              'permissions': r.permissions, 'colour': r.colour,
                                              'created_at': str(r.created_at), 'mention': r.mention,
                                              'members': r.members, })
            d[n]['id'] = m.id
            d[n]['webhook_id'] = m.webhook_id
            d[n]['attachments'] = []
            for a in m.attachments:
                d[n]['attachments'].append({'id': a.id, 'size': a.size, 'height': a.height, 'width': a.width,
                                            'filename': a.filename, 'url': a.url, 'proxy_url': a.proxy_url,
                                            'is_spoiler()': a.is_spoiler(), 'download_id': b})
                await a.save(f'attachments\\{b}_{a.filename}')
                b += 1
            d[n]['pinned'] = m.pinned
            d[n]['flags'] = []
            for f in m.flags:
                try:
                    d[n]['flags'].append({'value': f.value, 'crossposted': f.crossposted,
                                          'is_crossposted': f.is_crossposted, 'suppress_embeds': f.suppress_embeds,
                                          'source_message_deleted': f.source_message_deleted, 'urgent': f.urgent})
                except Exception:
                    pass
            d[n]['reactions'] = []
            for r in m.reactions:
                d[n]['reactions'].append({'emoji': str(r.emoji), 'count': r.count, 'me': r.me,
                                          'message': str(r.message), 'custom_emoji': r.custom_emoji})
            d[n]['activity'] = m.activity
            d[n]['application'] = m.application
            d[n]['guild'] = str(m.guild)
            d[n]['raw_mentions'] = m.raw_mentions
            d[n]['raw_channel_mentions'] = m.raw_channel_mentions
            d[n]['raw_role_mentions'] = m.raw_role_mentions
            d[n]['clean_content'] = m.clean_content
            d[n]['created_at'] = str(m.created_at)
            d[n]['edited_at'] = str(m.edited_at)
            d[n]['jump_url'] = m.jump_url
            d[n]['is_system()'] = m.is_system()
            d[n]['system_content'] = m.system_content
            print(f'Message {n} got dumped successfully.')
            n += 1
        json_dump(f'channels\\{c.id}.json', d)
        print(f'{c.name} dumped successfully.')
    print(f'Operation completed successfully in {time() - x}')
    exit()


@client.event
async def on_ready():
    await dump_channels()


client.run(TOKEN, bot=BOT)
