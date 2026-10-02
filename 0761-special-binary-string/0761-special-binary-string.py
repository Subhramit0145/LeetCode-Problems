class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        parts = []
        count = start = 0

        for i, ch in enumerate(s):
            count += 1 if ch == '1' else -1

            if count == 0:
                inner = self.makeLargestSpecial(s[start + 1:i])
                parts.append('1' + inner + '0')
                start = i + 1

        parts.sort(reverse=True)
        return ''.join(parts)