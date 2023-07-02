from models import guild, privacy_level, scheduled_event, stage_channel


def high(x):
    return {'channel': stage_channel.mid(x.channel), 'channel_id': x.channel_id,
            'discoverable_disabled': x.discoverable_disabled, 'guild': guild.mid(x.guild), 'id': x.id,
            'privacy_level': privacy_level.mid(x.privacy_level),
            'scheduled_event': scheduled_event.mid(x.scheduled_event),
            'scheduled_event_id': x.scheduled_event_id, 'topic': x.topic}


def mid(x):
    return {'channel': stage_channel.low(x.channel), 'channel_id': x.channel_id,
            'discoverable_disabled': x.discoverable_disabled, 'guild': guild.low(x.guild), 'id': x.id,
            'privacy_level': privacy_level.low(x.privacy_level),
            'scheduled_event': scheduled_event.low(x.scheduled_event),
            'scheduled_event_id': x.scheduled_event_id, 'topic': x.topic}


def low(x):
    return {'channel_id': x.channel_id, 'discoverable_disabled': x.discoverable_disabled, 'id': x.id,
            'scheduled_event_id': x.scheduled_event_id, 'topic': x.topic}
