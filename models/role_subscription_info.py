

def high(x):
    try:
        return {'is_renewal': x.is_renewal, 'role_subscription_listing_id': x.role_subscription_listing_id,
                'tier_name': x.tier_name, 'total_months_subscribed': x.total_months_subscribed}
    except AttributeError:
        return 'None'


def mid(x):
    try:
        return {'is_renewal': x.is_renewal, 'role_subscription_listing_id': x.role_subscription_listing_id,
                'tier_name': x.tier_name, 'total_months_subscribed': x.total_months_subscribed}
    except AttributeError:
        return 'None'


def low(x):
    try:
        return {'is_renewal': x.is_renewal, 'role_subscription_listing_id': x.role_subscription_listing_id,
                'tier_name': x.tier_name, 'total_months_subscribed': x.total_months_subscribed}
    except AttributeError:
        return 'None'
