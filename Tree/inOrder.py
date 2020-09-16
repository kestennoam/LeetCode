# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        s, ans = [], []
        cur = root
        while s or cur:
            if cur:
                s.append(cur)
                cur = cur.left
            else:
                cur = s.pop()
                ans.append(cur.val)
                cur = cur.right

        return ans
