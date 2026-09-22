class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix[0])
        dp = [0] * (n + 1)
        max_side = 0
        prev = 0

        for row in matrix:
            for j in range(1, n + 1):
                temp = dp[j]

                if row[j - 1] == "1":
                    dp[j] = 1 + min(dp[j], dp[j - 1], prev)
                    max_side = max(max_side, dp[j])
                else:
                    dp[j] = 0

                prev = temp

            prev = 0

        return max_side * max_side