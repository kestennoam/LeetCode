def plusOne(digits):
    """
    Given a non-empty array of digits representing a non-negative integer,
    increment one to the integer.
The digits are stored such that the most significant digit is at the
 head of the list, and each element in the array contains a single digit.
You may assume the integer does not contain any leading zero,
 except the number 0 itself.
    :param digits:
    :return:
    """
    flag = False  # boolean of changed
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] != 9:
            digits[i] += 1
            flag = True
            break
        # it's 9
        digits[i] = 0
    if not flag:
        digits.insert(0, 1)
    return digits
