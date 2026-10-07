class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = []
        visited = {s}
        q = [s]
        found = False

        while q:
            nxt = []

            for cur in q:
                bal = 0
                valid = True

                for ch in cur:
                    if ch == '(':
                        bal += 1
                    elif ch == ')':
                        bal -= 1
                        if bal < 0:
                            valid = False
                            break

                if valid and bal == 0:
                    res.append(cur)
                    found = True

                if found:
                    continue

                for i, ch in enumerate(cur):
                    if ch not in '()':
                        continue
                    if i > 0 and cur[i] == cur[i - 1]:
                        continue

                    ns = cur[:i] + cur[i + 1:]
                    if ns not in visited:
                        visited.add(ns)
                        nxt.append(ns)

            if found:
                return res

            q = nxt

        return res