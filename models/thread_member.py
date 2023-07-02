from models import datetime, thread


def high(x):
    return {'id': x.id, 'joined_at': datetime.mid(x.joined_at), 'thread': thread.mid(x.thread),
            'thread_id': x.thread_id}


def mid(x):
    return {'id': x.id, 'joined_at': datetime.low(x.joined_at), 'thread': thread.low(x.thread),
            'thread_id': x.thread_id}


def low(x):
    return {'id': x.id, 'thread_id': x.thread_id}
