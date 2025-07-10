class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        if len(s) != len(t):
            return False
        for a in s:
            if a in letters:
                letters[a] += 1
            else:
                letters[a] = 1
        for p in t:
            if p in letters:
                letters[p] -= 1
            else:
                return False 
            if letters[p] < 0:
                return False
        return True
