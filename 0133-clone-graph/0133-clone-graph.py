class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        clones = {node: Node(node.val)}
        stack = [node]

        while stack:
            curr = stack.pop()

            for nei in curr.neighbors:
                if nei not in clones:
                    clones[nei] = Node(nei.val)
                    stack.append(nei)

                clones[curr].neighbors.append(clones[nei])

        return clones[node]