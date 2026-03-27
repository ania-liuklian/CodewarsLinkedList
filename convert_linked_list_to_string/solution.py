class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
def stringify(node):
    result = ''
    if not isinstance(node, Node):
            return 'None'
    while node.next:
        result += str(node.data)
        result += ' -> '
        node = node.next
    result += str(node.data)
    result += ' -> '
    result += 'None'
    return result
