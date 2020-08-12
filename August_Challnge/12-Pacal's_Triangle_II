class Solution:
    def getRow(self, rowIndex: int):
        rows=[[1]]
        for i in range(rowIndex):
            rows.append([1]+[sum(pair) for pair in zip(rows[-1],rows[-1][1:])]+[1])
        return rows[-1]
