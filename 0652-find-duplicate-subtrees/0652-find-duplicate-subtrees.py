from collections import defaultdict
from typing import Optional

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        count = defaultdict(int)
        res = []

        def dfs(node):
            if not node:
                return 0

            key = (node.val, dfs(node.left), dfs(node.right))
            if key not in ids:
                ids[key] = len(ids) + 1

            uid = ids[key]
            count[uid] += 1

            if count[uid] == 2:
                res.append(node)

            return uid

        ids = {}
        dfs(root)
        return res