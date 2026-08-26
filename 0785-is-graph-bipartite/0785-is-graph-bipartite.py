class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [0] * len(graph)

        for start in range(len(graph)):
            if color[start]:
                continue

            color[start] = 1
            stack = [start]

            while stack:
                node = stack.pop()

                for nei in graph[node]:
                    if not color[nei]:
                        color[nei] = -color[node]
                        stack.append(nei)
                    elif color[nei] == color[node]:
                        return False

        return True