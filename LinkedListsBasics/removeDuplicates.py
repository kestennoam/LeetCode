class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class singlyLinkedList:
    def __init__(self):
        self.head = Node()
        self.size = 0


def removeDuplicatesWithMemory(lst):
    dup = set()
    cur = lst
    while cur and cur.next:
        dup.add(cur.val)
        while cur.next and cur.next.val in dup:
            cur.next = cur.next.next
        cur = cur.next



def removeDuplicatesNoMemory(lst):
    cur = lst
    while cur:
        runner = cur
        while runner:
            if runner.next and runner.next.val == cur.val:
                runner.next = runner.next.next
            else: runner = runner.next
        cur = cur.next




a = Node(1,Node(4,Node(5,Node(1,Node(1)))))

b = a
# while b:
#     # print(b.val)
#     b = b.next
removeDuplicatesNoMemory(a)
while a:
    print(a.val)
    a = a.next
