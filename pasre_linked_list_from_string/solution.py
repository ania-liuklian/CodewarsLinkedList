from preloaded import Node


def linked_list_from_string(list_repr: str) -> Node | None:
    items = list_repr.split(' -> ')[::-1]
    result = None
    for el in items:
        if el == 'None':
            result = None
        else:
            result = Node(int(el), result)
    return result
