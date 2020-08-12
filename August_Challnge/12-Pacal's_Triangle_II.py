class Solution:
    def getRow(self, rowIndex: int):
        rows = [[1]]
        for i in range(rowIndex):
            rows = [[1]
                    + [sum(pair) for pair in zip(rows[-1], rows[-1][1:])] +
                    [1]]
        return rows[0]


if __name__ == '__main__':
    sol = Solution()
    print(sol.getRow(4))
