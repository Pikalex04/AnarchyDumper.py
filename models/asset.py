from time import time


async def high(x, y):
    try:
        await x.save(f'dumps/{y}/assets/{round(time() * 1000)}')
        return {'key': x.key, 'url': x.url}
    except AttributeError:
        return 'None'


async def mid(x, y):
    try:
        await x.save(f'dumps/{y}/assets/{round(time() * 1000)}')
        return {'key': x.key, 'url': x.url}
    except AttributeError:
        return 'None'


def low(x):
    try:
        return {'key': x.key, 'url': x.url}
    except AttributeError:
        return 'None'

