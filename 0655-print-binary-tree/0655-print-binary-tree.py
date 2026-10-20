class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def height(node):
            if not node:
                return 0
            return 1 + max(height(node.left), height(node.right))

        h = height(root)
        m, n = h, (1 << h) - 1
        res = [[""] * n for _ in range(m)]

        def dfs(node, r, left, right):
            if not node:
                return
            mid = (left + right) // 2
            res[r][mid] = str(node.val)
            dfs(node.left, r + 1, left, mid - 1)
            dfs(node.right, r + 1, mid + 1, right)

        dfs(root, 0, 0, n - 1)
        return res