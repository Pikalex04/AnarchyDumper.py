from models import emoji, message, partial_emoji


def high(x):
    d = {'count': x.count, 'me': x.me, 'message': message.mid(x.message)}
    try:
        d['emoji'] = emoji.mid(x.emoji)
    except AttributeError:
        try:
            d['emoji'] = partial_emoji.mid(x.emoji)
        except AttributeError:
            d['emoji'] = x.emoji
    return d


def mid(x):
    d = {'count': x.count, 'me': x.me, 'message': message.low(x.message)}
    try:
        d['emoji'] = emoji.low(x.emoji)
    except AttributeError:
        try:
            d['emoji'] = partial_emoji.low(x.emoji)
        except AttributeError:
            d['emoji'] = x.emoji
    return d


def low(x):
    d = {'count': x.count, 'me': x.me}
    if str(x.emoji) == x.emoji:
        d['emoji'] = x.emoji
    return d
