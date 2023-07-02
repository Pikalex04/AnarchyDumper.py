from discord import Client, Intents
from json import dump, load
from time import time
from os import listdir, mkdir, remove
from sys import exit

from models import message


# JSON Functions
def json_load(n):
    with open(n, 'r') as f:
        a = load(f)
        f.close()
        return a


def json_dump(n, d):
    with open(n, 'w+') as f:
        dump(d, f)
        f.close()


# Dumping Functions


async def dump_channel(channel, output):
    messages = []
    d = 0
    n = 1
    try:
        mkdir(f'dumps/{output}/')
    except FileExistsError:
        pass
    try:
        mkdir(f'dumps/{output}/attachments/')
    except FileExistsError:
        pass
    try:
        mkdir(f'dumps/{output}/assets/')
    except FileExistsError:
        pass
    async for msg in channel.history(limit=None, oldest_first=True):
        messages.append(await message.custom(msg, channel.id))
        json_dump(f'dumps/{output}/{d:{"0"}{10}}_messages.json', messages)
        print(f'Message {n} dumped successfully.')
        n += 1
        if n / 100 == round(n / 100):
            d += 1
            messages = []
    final_dump = []
    for messages_dump in listdir(f'dumps/{output}/'):
        if messages_dump.endswith('_messages.json'):
            final_dump += json_load(f'dumps/{output}/{messages_dump}')
            remove(f'dumps/{output}/{messages_dump}')
    json_dump(f'dumps/{output}/messages.json', final_dump)
    print(f'Messages of {channel.id} dumped successfully.')
    try:
        async for thread in channel.archived_threads():
            await dump_channel(thread, f'{output}/{thread.id}')
    except Exception:
        pass
    else:
        print(f'Public threads of {output} dumped successfully.')
    print(f'{channel.id} dumped successfully.')


client = Client(intents=Intents.default().all())


async def start():
    x = time()
    meta = json_load('settings.json')['mode']
    if meta[0] == 0:  # Dump all the specified channels and their threads
        for channel in meta[1]:
            chn_obj = client.get_channel(channel)
            await dump_channel(chn_obj, chn_obj.id)
    elif meta[0] == 1:  # Dump all the channels and their threads inside a category
        for channel in client.get_channel(meta[1]).text_channels:
            chn_obj = client.get_channel(channel)
            await dump_channel(chn_obj, chn_obj.id)
    print(f'Operation completed successfully in {time() - x} seconds.')
    await client.close()


@client.event
async def on_connect():
    print(f'Client successfully connected to Discord as {client.user}!')


@client.event
async def on_ready():
    print('Ready! Starting dumping process...')
    await start()
    exit()


print('Loading...')

client.run(json_load('settings.json')['token'])
