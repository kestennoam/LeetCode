def moveZeroes(nums):
    """
    Given an array nums, write a function to move all 0's to the end of it
    while maintaining the relative order of the non-zero elements.
    Do not return anything, modify nums in-place instead.
    O(n) Time complexity
    O(1) Space memory
    """
    lastZero = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[lastZero] = nums[lastZero], nums[i]
            lastZero += 1