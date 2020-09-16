# singly linked list

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class singlyLinkedList:
    def __init__(self):
        self.head = Node()
        self.size = 0


class NodeDouble:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


