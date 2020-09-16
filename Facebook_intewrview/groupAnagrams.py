class Solution:
    """
    https://leetcode.com/explore/interview/card/facebook/5/array-and-strings/3014/
    Time O(n)
    """
    def groupAnagrams(self, strs):
        lst = []
        dic_save = {}
        i = 0
        for str in strs:
            sorted_str = ''.join(sorted(str))
            if sorted_str in dic_save:
                lst[dic_save[sorted_str]].append(str)
            else:
                lst.append([str])
                dic_save[sorted_str] = len(lst) - 1

        return lst
