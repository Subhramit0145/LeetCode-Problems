class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val):
            if not node:
                return 0

            count = node.val >= max_val
            max_val = max(max_val, node.val)

            return count + dfs(node.left, max_val) + dfs(node.right, max_val)

        return dfs(root, root.val)