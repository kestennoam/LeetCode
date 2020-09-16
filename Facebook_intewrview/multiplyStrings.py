import math

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num = 0
        for i in range(len(num1)):
            num = num * 10 + int(num1[i])

        product = 0
        for i in range(len(num2) - 1, -1, -1):
            temp = num * math.floor(long(num2[i])) * (10 ** (len(num2) - 1 - i))
            print(temp)
            product += temp
            print(product, "  product")
        strProduct = ""
        while product > 0:
            strProduct = str(product % 10) + strProduct
            product = math.floor(product / 10)
        return strProduct


a = Solution()
a.multiply("6913259244", "71103343")