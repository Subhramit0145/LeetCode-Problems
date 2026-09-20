class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        def valid(a, b):
            if (a[0] == '0' and len(a) > 1) or (b[0] == '0' and len(b) > 1):
                return False

            i, j = len(a), len(b)
            x, y = int(a), int(b)

            while i + j < n:
                z = x + y
                z_str = str(z)

                if not num[i + j:].startswith(z_str):
                    return False

                i += j
                j = len(z_str)
                x, y = y, z

            return i + j == n

        for i in range(1, n):
            if num[0] == '0' and i > 1:
                break

            for j in range(i + 1, n):
                if num[i] == '0' and j - i > 1:
                    break

                if valid(num[:i], num[i:j]):
                    return True

        return False