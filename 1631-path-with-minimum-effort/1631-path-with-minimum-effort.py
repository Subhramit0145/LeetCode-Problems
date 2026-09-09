class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        left, right = 0, max(max(row) for row in heights) - min(min(row) for row in heights)

        def can_reach(limit):
            stack = [(0, 0)]
            seen = {(0, 0)}

            while stack:
                r, c = stack.pop()

                if r == m - 1 and c == n - 1:
                    return True

                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc

                    if (
                        0 <= nr < m and 0 <= nc < n
                        and (nr, nc) not in seen
                        and abs(heights[nr][nc] - heights[r][c]) <= limit
                    ):
                        seen.add((nr, nc))
                        stack.append((nr, nc))

            return False

        while left < right:
            mid = (left + right) // 2

            if can_reach(mid):
                right = mid
            else:
                left = mid + 1

        return left