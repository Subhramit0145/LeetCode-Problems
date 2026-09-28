class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7
        dp = [[0] * n for _ in range(m)]
        dp[startRow][startColumn] = 1
        ans = 0

        for _ in range(maxMove):
            nxt = [[0] * n for _ in range(m)]

            for r in range(m):
                for c in range(n):
                    if dp[r][c]:
                        val = dp[r][c]

                        if r == 0:
                            ans = (ans + val) % MOD
                        else:
                            nxt[r - 1][c] = (nxt[r - 1][c] + val) % MOD

                        if r == m - 1:
                            ans = (ans + val) % MOD
                        else:
                            nxt[r + 1][c] = (nxt[r + 1][c] + val) % MOD

                        if c == 0:
                            ans = (ans + val) % MOD
                        else:
                            nxt[r][c - 1] = (nxt[r][c - 1] + val) % MOD

                        if c == n - 1:
                            ans = (ans + val) % MOD
                        else:
                            nxt[r][c + 1] = (nxt[r][c + 1] + val) % MOD

            dp = nxt

        return ans