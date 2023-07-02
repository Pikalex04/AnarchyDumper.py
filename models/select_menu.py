from models import channel_type, component_type, select_option


def high(x):
    return {'channel_types': [channel_type.mid(y) for y in x.channel_types], 'custom_id': x.custom_id,
            'disabled': x.disabled, 'max_values': x.max_values,  'min_values': x.min_values,
            'options': [select_option.mid(y) for y in x.option], 'placeholder': x.placeholder,
            'type': component_type.mid(x.type)}


def mid(x):
    return {'channel_types': [channel_type.low(y) for y in x.channel_types], 'custom_id': x.custom_id,
            'disabled': x.disabled, 'max_values': x.max_values,  'min_values': x.min_values,
            'options': [select_option.low(y) for y in x.option], 'placeholder': x.placeholder,
            'type': component_type.low(x.type)}


def low(x):
    return {'custom_id': x.custom_id, 'disabled': x.disabled, 'max_values': x.max_values,  'min_values': x.min_values,
            'placeholder': x.placeholder}
