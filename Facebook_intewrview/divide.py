class Solution:
    intMax = (2 ** 31) - 1

    def divide(self, dividend: int, divisor: int) -> int:
        sgn = 1
        if (divisor < 0 and dividend > 0):
            sgn, divisor = -1,  - divisor
        elif (divisor > 0 and dividend < 0):
            sgn, dividend = -1, - dividend

        if dividend < divisor:
            return 0

        c = 1

        while dividend > divisor:
            c += 1
            divisor += divisor

        return c if sgn == 1 else - c


a = Solution()
print(a.divide(-1, 1))
