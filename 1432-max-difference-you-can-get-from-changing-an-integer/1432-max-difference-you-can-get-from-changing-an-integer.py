class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)

        a = s
        for ch in s:
            if ch != '9':
                a = s.replace(ch, '9')
                break

        b = s
        if s[0] != '1':
            b = s.replace(s[0], '1')
        else:
            for ch in s[1:]:
                if ch not in '01':
                    b = s.replace(ch, '0')
                    break

        return int(a) - int(b)