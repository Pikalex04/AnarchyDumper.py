from time import time


async def high(x, y, z):
    await x.save(f'dumps/{y}/attachments/{round(time() * 1000)}__{z}__{x.filename}')
    return {'content_type': x.content_type, 'description': x.description, 'duration': x.duration,
            'ephemeral': x.ephemeral, 'filename': x.filename, 'height': x.height, 'id': x.id, 'proxy_url': x.proxy_url,
            'size': x.size, 'url': x.url, 'waveform': x.waveform, 'width': x.width}


async def mid(x, y, z):
    await x.save(f'dumps/{y}/attachments/{round(time() * 1000)}__{z}__{x.filename}')
    return {'content_type': x.content_type, 'description': x.description, 'duration': x.duration,
            'ephemeral': x.ephemeral, 'filename': x.filename, 'height': x.height, 'id': x.id, 'proxy_url': x.proxy_url,
            'size': x.size, 'url': x.url, 'waveform': x.waveform, 'width': x.width}


def low(x):
    return {'content_type': x.content_type, 'description': x.description, 'duration': x.duration,
            'ephemeral': x.ephemeral, 'filename': x.filename, 'height': x.height, 'id': x.id, 'proxy_url': x.proxy_url,
            'size': x.size, 'url': x.url, 'waveform': x.waveform, 'width': x.width}
