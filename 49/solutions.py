class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def isAnagram(s: str, t: str) -> bool:
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
        
        used = [False] * len(strs)
        output = []
        for i, word in enumerate(strs):
            if used[i]:
                continue
            group = [word]
            used[i] = True
            for j in range(i+1,len(strs)):
                if not used[j] and isAnagram(word,strs[j]):
                    group.append(strs[j])
                    used[j] = True
            output.append(group)
        return output
