class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        chars_freq = {}
        for ch in s:
            chars_freq[ch] = chars_freq.get(ch,0)+1
        
        for ch in t :
            if ch not in chars_freq:
                return False
            else:
                if chars_freq[ch] == 0:
                    return False
            chars_freq[ch]-=1
        return True