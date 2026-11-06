class Solution:
    def maxDepth(self, s: str) -> int:
        current=0
        max_depth = 0
        for brac in s:
            if(brac =='('):
                current+=1
                max_depth = max(max_depth, current)
            elif(brac ==')'):
                current -=1
        return max_depth