class Solution:
    """
    Time Complexity: O(M + N)O(M+N), where M, NM,N are the lengths of A and B respectively.

    Space Complexity: O(M + N)O(M+N), the maximum size of the answer.
    """

    def intervalIntersection(self, A, B):
        i, j = 0, 0
        ans = []
        while i < len(A) and j < len(B):
            low = max(A[i][0], B[j][0])
            high = min(A[i][1], B[j][1])
            if low <= high:
                ans.append([low, high])

            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1

        return ans
