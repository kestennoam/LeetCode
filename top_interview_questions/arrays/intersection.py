def intersect(nums1, nums2):
    """
    Given two arrays, write a function to compute their intersection.

    O(n+m) complexity
    O(min(m,n) Complexity
    :param nums1:
    :param nums2:
    :return:
    """
    crossedArr = []
    dic = {}
    for num in nums1:
        if not num in dic:
            dic[num] = 1
        else:
            dic[num] += 1
    for num in nums2:
        if num in dic and dic[num] > 0:
            dic[num] -= 1
            crossedArr.append(num)

    return crossedArr
