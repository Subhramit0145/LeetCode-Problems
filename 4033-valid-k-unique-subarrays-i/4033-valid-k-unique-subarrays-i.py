from typing import List
from math import isqrt

class Solution:
    def validSubarrays(self, nums: List[int], k: int, queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        block = max(1, isqrt(n))
        indexed = sorted(
            [(l, r, i) for i, (l, r) in enumerate(queries)],
            key=lambda q: (q[0] // block, q[1] if (q[0] // block) % 2 == 0 else -q[1])
        )

        freq = {}
        distinct = 0
        odd = 0
        left, right = 0, -1
        ans = [False] * len(queries)

        def add(i):
            nonlocal distinct, odd
            x = nums[i]
            f = freq.get(x, 0)
            if f == 0:
                distinct += 1
            odd += 1 if f % 2 == 0 else -1
            freq[x] = f + 1

        def remove(i):
            nonlocal distinct, odd
            x = nums[i]
            f = freq[x]
            odd += 1 if f % 2 == 0 else -1
            if f == 1:
                del freq[x]
                distinct -= 1
            else:
                freq[x] = f - 1

        for l, r, idx in indexed:
            while left > l:
                left -= 1
                add(left)
            while right < r:
                right += 1
                add(right)
            while left < l:
                remove(left)
                left += 1
            while right > r:
                remove(right)
                right -= 1

            ans[idx] = distinct == k and odd == 0

        return ans