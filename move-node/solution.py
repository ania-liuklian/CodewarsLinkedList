class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source, dest):
    front = source.data
    source = source.next
    dest_new = Node(front)
    dest_new.next = dest
    return Context(source, dest_new)
