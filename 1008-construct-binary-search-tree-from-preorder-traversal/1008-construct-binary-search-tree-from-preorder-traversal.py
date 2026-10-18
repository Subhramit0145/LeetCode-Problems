class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        i = 0

        def build(bound):
            nonlocal i
            if i == len(preorder) or preorder[i] > bound:
                return None

            root = TreeNode(preorder[i])
            i += 1
            root.left = build(root.val)
            root.right = build(bound)
            return root

        return build(float('inf'))