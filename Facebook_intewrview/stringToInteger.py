class Solution:
    INT_MAX = (2 ** 31) - 1
    INT_MIN = -(2 ** 31)
    SPACE = ' '

    def myAtoi(self, str: str) -> int:
        """
    https://leetcode.com/explore/interview/card/facebook/5/array-and-strings/3009/

    Implement atoi which converts a string to an integer.
    The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.
    The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.
    If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
    If no valid conversion could be performed, a zero value is returned.

    TIme complexity- O(n)
    SPace - O(1)
    Note:

    Only the space character ' ' is considered as whitespace character.
    Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
        :param str:
        :return:
        """
        i = 0
        while i < len(str):
            if str[i] == self.SPACE:
                i += 1
            else:
                break

        if i >= len(str):
            return 0  # edge case of just spaces

        sgn = '+'
        if str[i] == '+' or str[i] == '-':
            sgn = str[i]
            i += 1
        num = 0
        for j in range(i, len(str)):
            if not str[j].isdigit(): break
            num = num * 10 + int(str[j])

        if num > self.INT_MAX:
            return self.INT_MAX if sgn == '+' else self.INT_MIN
        return num if sgn == '+' else num * -1
