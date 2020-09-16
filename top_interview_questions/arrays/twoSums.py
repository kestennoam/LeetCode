def twoSum(nums, target) :
    dicDiffs = {}
    for i, num in enumerate(nums):
        if num in dicDiffs:
            return [dicDiffs[num], i]
        else:  # not in dic
            dicDiffs[target - num] = i