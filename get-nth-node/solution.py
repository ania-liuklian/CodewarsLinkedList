from preloaded import Node

# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next

def get_len(node):
    lenght = 0
    current = node
    while current:
        lenght += 1
        current = current.next
    return lenght
def get_nth(node, index):
    if index < 0 or index > get_len(node) - 1:
        raise IndexError
    if index == 0:
        return node
    if node:
        current = node
        count = 0
    else:
        raise ValueError
    while current:
        if count == index:
            return current
        current = current.next
        count += 1
