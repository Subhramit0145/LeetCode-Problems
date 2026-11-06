class Solution:
    def frequencySort(self, s: str) -> str:
        result = ""
        mapp = {}
        for ch in s:
            mapp[ch] = mapp.get(ch, 0)+1
        sorted_map = sorted(mapp.items(), key = lambda x: (-x[1], x[0]))
        for ch, freq in sorted_map:
            result += (ch*freq)
        return result
