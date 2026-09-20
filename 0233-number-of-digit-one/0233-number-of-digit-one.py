class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        factor = 1

        while factor <= n:
            high = n // (factor * 10)
            cur = (n // factor) % 10
            low = n % factor

            if cur == 0:
                count += high * factor
            elif cur == 1:
                count += high * factor + low + 1
            else:
                count += (high + 1) * factor

            factor *= 10

        return count