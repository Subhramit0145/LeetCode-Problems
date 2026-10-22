class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        q = deque([root])

        while q:
            level_max = float('-inf')

            for _ in range(len(q)):
                node = q.popleft()
                level_max = max(level_max, node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(level_max)

        return res