class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = {}
        for a in magazine:
            if a in letters:
                letters[a] += 1
            else:
                letters[a] = 1
        for p in ransomNote:
            if p in letters:
                letters[p] -= 1
            else:
                return False
            if letters[p] < 0:
                return False
        return True
            
        
