class Solution:
    def maximumLength(self, s: str) -> int:
        groups = [[] for _ in range(26)]
        n = len(s)
        i = 0

        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            groups[ord(s[i]) - 97].append(j - i)
            i = j

        ans = -1
        for lengths in groups:
            if not lengths:
                continue

            lengths.sort(reverse=True)
            a = lengths[0]
            b = lengths[1] if len(lengths) > 1 else 0
            c = lengths[2] if len(lengths) > 2 else 0

            ans = max(ans, a - 2, min(a - 1, b), c)

        return ans if ans > 0 else -1