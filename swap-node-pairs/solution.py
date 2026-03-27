from preloaded import Node

def swap_pairs(head):
    if not head:
        return None
    if not head.next:
        return head
    new_head = head.next
    prev = None
    curr = head
    while curr and curr.next:
        first = curr
        second = curr.next
        first.next = second.next
        second.next = first

        if prev:
            prev.next = second

        prev = first
        curr = first.next

    return new_head
