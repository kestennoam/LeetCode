# def containsDuplicate(nums) :
#     dupSet = set()
#     for num in nums:
#         if num in dupSet: return True
#         dupSet.add(num)
#     return False


def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    return True if len(set(nums)) < len(nums) else False
