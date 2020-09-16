# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode):
        s, ans = [], []
        cur = root
        while s or cur:
            if cur:
                s.append(cur)
                ans.append(cur.val)
                cur = cur.left
            else:
                cur = s.pop()
                cur = cur.right

        return ans


if __name__ == '__main__':
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t6 = TreeNode(6)
    t7 = TreeNode(7)
    t3.left, t3.right = t2, t4
    t4.right= t7
    t2.left= t1

    sol = Solution()
    print(sol.preorderTraversal(t3))

