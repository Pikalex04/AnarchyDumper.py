from models import button, component_type, select_menu


def high(x):
    d = {'type': component_type.mid(x.type), 'children': []}
    for child in x.children:
        if str(child.type) == 'ComponentType.action_row':
            d['children'].append(mid(x))
        elif str(child.type) == 'ComponentType.button':
            d['children'].append(button.mid(child))
        else:
            d['children'].append(select_menu.mid(child))
    return d


def mid(x):
    d = {'type': component_type.low(x.type), 'children': []}
    for child in x.children:
        if str(child.type) == 'ComponentType.action_row':
            d['children'].append(low())
        elif str(child.type) == 'ComponentType.button':
            d['children'].append(button.low(child))
        else:
            d['children'].append(select_menu.low(child))
    return d


def low():
    return {}
