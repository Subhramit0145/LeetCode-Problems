class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        m, n = len(cost), len(cost[0])
        INF = float('inf')
        dp = [INF] * (1 << n)
        dp[0] = 0

        for i in range(m):
            ndp = [INF] * (1 << n)

            for mask in range(1 << n):
                if dp[mask] == INF:
                    continue

                for j in range(n):
                    new_mask = mask | (1 << j)
                    ndp[new_mask] = min(
                        ndp[new_mask],
                        dp[mask] + cost[i][j]
                    )

            dp = ndp

        min_cost = [min(cost[i][j] for i in range(m)) for j in range(n)]

        for mask in range(1 << n):
            extra = sum(
                min_cost[j]
                for j in range(n)
                if not (mask & (1 << j))
            )
            dp[mask] += extra

        return min(dp)