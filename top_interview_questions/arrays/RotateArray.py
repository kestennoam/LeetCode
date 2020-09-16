# def rotate(nums, k) :
#     """
#     O(nk) solution
#     O(1) Memory
#     """
#     if not nums: return  # edge case
#     while k > 0:
#         temp = nums[-1]
#         for j in range(len(nums) - 2, -1, -1):
#             nums[j + 1] = nums[j]
#         nums[0] = temp
#         k -= 1

# ------------------------------------------
#     Best way !
#     reverse all the list,
#     then reverse just the first k elements and then the n-k elements
#      O(n) Time complexity and O(1) Memory

def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start, end = start + 1, end - 1


def rotate(nums, k):
    n = len(nums)
    k %= n

    reverse(nums, 0, n - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, n - 1)


arr = [1, 2, 3, 4, 5, 6, 7]
rotate(arr, 3)
print(arr)
