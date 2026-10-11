class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        import heapq

        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2
        total = sum(diffs)

        if k >= total:
            return 0

        freq = [0] * (max(diffs) + 1)
        for d in diffs:
            freq[d] += 1

        for d in range(len(freq) - 1, 0, -1):
            if k >= freq[d]:
                k -= freq[d]
                freq[d - 1] += freq[d]
                freq[d] = 0
            else:
                freq[d] -= k
                freq[d - 1] += k
                k = 0
                break

        return sum(d * d * count for d, count in enumerate(freq))