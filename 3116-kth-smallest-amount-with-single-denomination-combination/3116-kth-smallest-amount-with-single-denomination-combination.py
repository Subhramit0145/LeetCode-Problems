from math import lcm
from functools import reduce

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        coins = sorted(coins)
        filtered = []

        for c in coins:
            if not any(c % x == 0 for x in filtered):
                filtered.append(c)

        coins = filtered
        m = len(coins)

        subsets = []
        for mask in range(1, 1 << m):
            val = 1
            bits = 0

            for i in range(m):
                if mask & (1 << i):
                    val = lcm(val, coins[i])
                    bits += 1

            subsets.append((val, 1 if bits % 2 else -1))

        def count(x):
            total = 0
            for val, sign in subsets:
                total += sign * (x // val)
            return total

        left, right = 1, min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left