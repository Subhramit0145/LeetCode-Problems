class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        return [i % 2 if ch == '(' else (i + 1) % 2 for i, ch in enumerate(seq)]