import heapq

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        def dijkstra(src):
            dist = [float('inf')] * n
            dist[src] = 0
            heap = [(0, src)]

            while heap:
                d, u = heapq.heappop(heap)
                if d > dist[u]:
                    continue

                for v, w in graph[u]:
                    nd = d + w
                    if nd < dist[v] and nd <= distanceThreshold:
                        dist[v] = nd
                        heapq.heappush(heap, (nd, v))

            return sum(d <= distanceThreshold for d in dist) - 1

        ans = -1
        min_count = float('inf')

        for city in range(n):
            count = dijkstra(city)
            if count <= min_count:
                min_count = count
                ans = city

        return ans