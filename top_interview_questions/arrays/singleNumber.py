def singleNumber(nums):
    """
    Given a non-empty array of integers, every element appears twice except
    for one. Find that single one.
    O(n) time complexity and memory
    :param nums:
    :return:
    """
    return 2 * sum(set(nums)) - sum(nums)
