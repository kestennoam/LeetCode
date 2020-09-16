# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        sentisel = ListNode(0, head)
        cur = head
        while cur:
            for i in range(m - 1):
                if not cur or not cur.next:
                    break
                cur = cur.next
            for i in range(n):
                if not cur.next:
                    break
                cur.next = cur.next.next
            cur = cur.next

        return sentisel.next







def decompressRLElist(nums) :
    ans = []
    for i in range(0, len(nums), 2):
        ans.append(nums[i + 1] for j in range(nums[i]))
    return ans


print(decompressRLElist([1,2,3,4]))