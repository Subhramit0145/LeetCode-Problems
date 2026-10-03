class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        MOD = 10**9 + 7
        count = [0] * 101

        for x in arr:
            count[x] += 1

        ans = 0

        for i in range(101):
            if count[i] == 0:
                continue

            for j in range(i, 101):
                if count[j] == 0:
                    continue

                k = target - i - j

                if k < j or k > 100 or count[k] == 0:
                    continue

                if i == j == k:
                    ans += count[i] * (count[i] - 1) * (count[i] - 2) // 6
                elif i == j:
                    ans += count[i] * (count[i] - 1) // 2 * count[k]
                elif j == k:
                    ans += count[j] * (count[j] - 1) // 2 * count[i]
                else:
                    ans += count[i] * count[j] * count[k]

        return ans % MOD