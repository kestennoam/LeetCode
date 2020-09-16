# class Solution:
#     def powerfulIntegers(self, x: int, y: int, bound: int):
#         ans = set()
#         self.helper(ans, x, y, 0, 0, bound)
#         return list(ans)
#
#     def helper(self, ans, x, y, i, j, bound):
#         cur = (x ** i) + (y ** j)
#         if cur > bound:
#             return
#         else:
#             ans.add(cur)
#             self.helper(ans, x, y, i + 1, j, bound)
#             self.helper(ans, x, y, i, j + 1, bound)
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int):
        ans = set()
        i, j = 0, 0
        while True:
            if ((x ** i) + (y ** j)) > bound:
                break
            else:
                ans.add((x ** i) + (y ** j))
                if pow(x, (i + 1)) + pow(y, j) <= bound:
                    ans.add(pow(x, (i + 1)) + pow(y, j))
                if pow(x, i) + pow(y, j + 1) <= bound:
                    ans.add(pow(x, i) + pow(y, j + 1))
            i += 1
            j += 1

        return list(ans)


a = Solution()
print(a.powerfulIntegers(2, 3, 10))
