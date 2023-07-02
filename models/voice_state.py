from models import datetime, stage_channel, voice_channel


def high(x):
    return {'afk': x.afk,
            'channel': voice_channel.mid(x.channel) if str(x.channel.type) == 'voice' else stage_channel.mid(x.channel),
            'deaf': x.deaf, 'mute': x.mute, 'requested_to_speak_at': datetime.mid(x.requested_to_speak_at),
            'self_deaf': x.self_deaf, 'self_mute': x.self_mute, 'self_stream': x.self_stream,
            'self_video': x.self_video, 'suppress': x.suppress}


def mid(x):
    return {'afk': x.afk,
            'channel': voice_channel.low(x.channel) if str(x.channel.type) == 'voice' else stage_channel.low(x.channel),
            'deaf': x.deaf, 'mute': x.mute, 'requested_to_speak_at': datetime.low(x.requested_to_speak_at),
            'self_deaf': x.self_deaf, 'self_mute': x.self_mute, 'self_stream': x.self_stream,
            'self_video': x.self_video, 'suppress': x.suppress}


def low(x):
    return {'afk': x.afk, 'deaf': x.deaf, 'mute': x.mute, 'self_deaf': x.self_deaf, 'self_mute': x.self_mute,
            'self_stream': x.self_stream, 'self_video': x.self_video, 'suppress': x.suppress}
