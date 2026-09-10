from collections import defaultdict
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, price in flights:
            graph[u].append((v, price))

        heap = [(0, src, 0)]
        best = {}

        while heap:
            cost, city, stops = heapq.heappop(heap)

            if city == dst:
                return cost

            if stops > k:
                continue

            if (city, stops) in best and best[(city, stops)] <= cost:
                continue

            best[(city, stops)] = cost

            for nxt, price in graph[city]:
                heapq.heappush(heap, (cost + price, nxt, stops + 1))

        return -1