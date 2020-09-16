class Solution:
    def nextPermutation(nums):
        """
        Implement next permutation, which rearranges numbers into the
        lexicographically next greater permutation of numbers.
        If such arrangement is not possible, it must rearrange it as the lowest
        possible order (ie, sorted in ascending order).
        The replacement must be in-place and use only constant extra memory.
        Here are some examples. Inputs are in the left-hand column and
         its corresponding outputs are in the right-hand column.


        Time Complexity O(n)
        Space O(1)
        https://leetcode.com/problems/next-permutation/

        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        tempMin = len(nums) - 1
        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1

        if i > 0:
            j = len(nums) - 1
            while j > 0 and nums[i - 1] >= nums[j]:
                j -= 1
            nums[i - 1], nums[j] = nums[j], nums[i - 1]

        j = len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
