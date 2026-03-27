class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def push(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node

def reverse(head):
    current = head
    reversed = None
    while current:
        new_node = Node(current.data)
        new_node.next = reversed
        reversed = new_node
        current = current.next
    return reversed

def alternating_split(head):
    if not head or not head.next:
        raise ValueError

    first = None
    second = None


    while head and head.next:
        first = push(first, head.data)
        second = push(second, head.next.data)
        head =head.next.next
    if head:
        first = push(first, head.data)
    first = reverse(first)
    second = reverse(second)
    return Context(first, second)
    
