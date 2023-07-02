from models import asset, datetime, entity_type, event_status, guild, privacy_level, stage_channel, user, \
    voice_channel


async def high(x):
    return {'channel': voice_channel.mid(x.afk_channel) if str(x.afk_channel.type) == 'voice' else
            stage_channel.mid(x.afk_channel),
            'cover_image': await asset.mid(x.cover_image, f'scheduled_event__cover_image__{x.id}'),
            'creator': user.mid(x.creator), 'creator_id': x.creator_id, 'description': x.description,
            'end_time': datetime.mid(x.end_time), 'entity_id': x.entity_id,
            'entity_type': entity_type.mid(x.entity_type),
            'guild': guild.mid(x.guild), 'id': x.id, 'location': x.location, 'name': x.name,
            'privacy_level': privacy_level.mid(x.privacy_level), 'start_time': datetime.mid(x.start_time),
            'status': event_status.mid(x.status), 'url': x.url, 'user_count': x.user_count}


def mid(x):
    return {'channel': voice_channel.low(x.afk_channel) if str(x.afk_channel.type) == 'voice' else
            stage_channel.low(x.afk_channel), 'cover_image': asset.low(x.cover_image), 'creator': user.low(x.creator),
            'creator_id': x.creator_id, 'description': x.description, 'end_time': datetime.low(x.end_time),
            'entity_id': x.entity_id, 'entity_type': entity_type.low(x.entity_type), 'guild': guild.low(x.guild),
            'id': x.id, 'location': x.location, 'name': x.name, 'privacy_level': privacy_level.low(x.privacy_level),
            'start_time': datetime.low(x.start_time), 'status': event_status.low(x.status), 'url': x.url,
            'user_count': x.user_count}


def low(x):
    return {'creator_id': x.creator_id, 'description': x.description, 'entity_id': x.entity_id, 'id': x.id,
            'location': x.location, 'name': x.name, 'url': x.url, 'user_count': x.user_count}
