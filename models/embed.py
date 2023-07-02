from models import color, datetime


def high(x):
    return {'author': str(x.author), 'color': color.mid(x.color), 'description': x.description,
            'fields': [str(y) for y in x.fields], 'footer': str(x.footer), 'image': str(x.image),
            'provider': str(x.provider), 'thumbnail': str(x.thumbnail), 'timestamp': datetime.mid(x.timestamp),
            'title': x.title, 'type': x.type, 'url': x.url, 'video': str(x.video)}


def mid(x):
    return {'author': str(x.author), 'color': color.low(x.color), 'description': x.description,
            'fields': [str(y) for y in x.fields], 'footer': str(x.footer), 'image': str(x.image),
            'provider': str(x.provider), 'thumbnail': str(x.thumbnail), 'timestamp': datetime.low(x.timestamp),
            'title': x.title, 'type': x.type, 'url': x.url, 'video': str(x.video)}


def low(x):
    return {'description': x.description, 'title': x.title, 'type': x.type, 'url': x.url}
