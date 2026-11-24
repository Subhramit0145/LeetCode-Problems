class Solution:
    def uniqueLetterString(self, s: str) -> int:
        last = {}
        ans = 0

        for i, c in enumerate(s):
            prev, prev2 = last.get(c, (-1, -1))
            ans += (i - prev) * (prev - prev2)
            last[c] = (i, prev)

        for prev, prev2 in last.values():
            ans += (len(s) - prev) * (prev - prev2)

        return ans