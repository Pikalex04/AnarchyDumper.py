from json import load
from os import listdir, mkdir


print('Loading...')


def json_load(n):
    with open(n, 'r') as f:
        a = load(f)
        f.close()
        return a


def format_datetime(dt_obj):
    try:
        return f'{dt_obj["d"]}/{dt_obj["m"]}/{dt_obj["y"]} {dt_obj["h"]}:{dt_obj["mi"]}'
    except KeyError:
        return 'None'


for folder in listdir(f'dumps/'):
    try:
        mkdir(f'output/{folder}')
    except FileExistsError:
        pass
    try:
        messages = json_load(f'dumps/{folder}/messages.json')
    except FileNotFoundError:
        pass
    else:
        content = ''
        for message in messages:
            content += f'{message["author"]["display_name"]}'
            if message['author']['bot']:
                content += ' [BOT]'
            content += f'   {format_datetime(message["created_at"])}\n\n'
            content += f'{message["content"]}'
            if message['edited_at'] != {}:
                content += ' (edited)'
            if message['attachments']:
                content += '\n'
                for attachment in message['attachments']:
                    content += f'\n## ATTACHMENT ({attachment["filename"]}) ##'
            if message['stickers']:
                content += '\n'
                for sticker in message['stickers']:
                    content += f'\n## STICKER ({sticker["name"]}) ##'
            for embed in message['embeds']:
                content += '\n\n## EMBED ##'
                content += f'{embed["author"]}\n' if embed['author'] != 'EmbedProxy()' else ''
                content += f'{embed["title"]}\n' if embed['title'] != 'EmbedProxy()' else ''
                content += f'{embed["description"]}\n' if embed['description'] != 'EmbedProxy()' else ''
                for field in embed['fields']:
                    content += f'{field}\n' if field != 'EmbedProxy()' else ''
                if embed['timestamp'] != {}:
                    content += f'{embed["footer"]}\n' if embed['description'] != 'EmbedProxy()' else ''
                else:
                    content += f'{embed["description"]} ' if embed['description'] != 'EmbedProxy()' else ''
                    content += format_datetime(embed['timestamp'])
            if message['reactions']:
                content += '\n\n'
                for reaction in message['reactions']:
                    content += f'{reaction["emoji"]} {reaction["count"]}'
            content += '\n\n\n\n'
        with open(f'output/{folder}/clean_messages.txt', 'w+', encoding="utf-8") as f:
            f.write(content)
    for subfolder in listdir(f'dumps/{folder}/'):
        if subfolder not in ['assets', 'attachments', 'messages.json']:
            messages = json_load(f'dumps/{folder}/{subfolder}/messages.json')
            content = ''
            for message in messages:
                content += f'{message["author"]["display_name"]}'
                if message['author']['bot']:
                    content += ' [BOT]'
                content += f'   {format_datetime(message["created_at"])}\n\n'
                content += f'{message["content"]}'
                if message['edited_at'] != {}:
                    content += ' (edited)'
                if message['attachments']:
                    content += '\n'
                    for attachment in message['attachments']:
                        content += f'\n## ATTACHMENT ({attachment["filename"]}) ##'
                if message['stickers']:
                    content += '\n'
                    for sticker in message['stickers']:
                        content += f'\n## STICKER ({sticker["name"]}) ##'
                for embed in message['embeds']:
                    content += '\n\n## EMBED ##'
                    content += f'{embed["author"]}\n' if embed['author'] != 'EmbedProxy()' else ''
                    content += f'{embed["title"]}\n' if embed['title'] != 'EmbedProxy()' else ''
                    content += f'{embed["description"]}\n' if embed['description'] != 'EmbedProxy()' else ''
                    for field in embed['fields']:
                        content += f'{field}\n' if field != 'EmbedProxy()' else ''
                    if embed['timestamp'] != {}:
                        content += f'{embed["footer"]}\n' if embed['description'] != 'EmbedProxy()' else ''
                    else:
                        content += f'{embed["description"]} ' if embed['description'] != 'EmbedProxy()' else ''
                        content += format_datetime(embed['timestamp'])
                if message['reactions']:
                    content += '\n\n'
                    for reaction in message['reactions']:
                        content += f'{reaction["emoji"]} {reaction["count"]}'
                content += '\n\n\n\n'
            try:
                mkdir(f'output/{folder}/{subfolder}/')
            except FileExistsError:
                pass
            with open(f'output/{folder}/{subfolder}/clean_messages.txt', 'w+', encoding="utf-8") as f:
                f.write(content)
