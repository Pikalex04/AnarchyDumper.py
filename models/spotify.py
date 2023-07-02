from models import activity_type, color, datetime, timedelta


def high(x):
    return {'album': x.album, 'album_cover_url': x.album_cover_url, 'artist': x.artist,
            'artists': [y for y in x.artists], 'color': color.mid(x.color), 'colour': color.mid(x.color),
            'created_at': datetime.mid(x.created_at), 'duration': timedelta.mid(x.duration), 'end': datetime.mid(x.end),
            'name': x.name, 'party_id': x.party_id, 'start': datetime.mid(x.start), 'title': x.title,
            'track_id': x.track_id, 'track_url': x.track_url, 'type': activity_type.mid(x.type)}


def mid(x):
    return {'album': x.album, 'album_cover_url': x.album_cover_url, 'artist': x.artist,
            'artists': [y for y in x.artists], 'color': color.low(x.color), 'colour': color.low(x.color),
            'created_at': datetime.low(x.created_at), 'duration': timedelta.low(x.duration), 'end': datetime.low(x.end),
            'name': x.name, 'party_id': x.party_id, 'start': datetime.low(x.start), 'title': x.title,
            'track_id': x.track_id, 'track_url': x.track_url, 'type': activity_type.low(x.type)}


def low(x):
    return {'album': x.album, 'album_cover_url': x.album_cover_url, 'artist': x.artist,
            'artists': [y for y in x.artists], 'name': x.name, 'party_id': x.party_id, 'title': x.title,
            'track_id': x.track_id, 'track_url': x.track_url}
