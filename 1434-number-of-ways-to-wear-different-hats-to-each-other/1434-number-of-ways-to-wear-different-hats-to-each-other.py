class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(hats)
        full = (1 << n) - 1

        hat_to_people = [[] for _ in range(41)]

        for person, choices in enumerate(hats):
            for hat in choices:
                hat_to_people[hat].append(person)

        dp = [0] * (1 << n)
        dp[0] = 1

        for hat in range(1, 41):
            for mask in range(full, -1, -1):
                if dp[mask] == 0:
                    continue

                for person in hat_to_people[hat]:
                    bit = 1 << person

                    if not (mask & bit):
                        new_mask = mask | bit
                        dp[new_mask] = (dp[new_mask] + dp[mask]) % MOD

        return dp[full]