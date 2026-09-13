class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sc, tc = defaultdict(int), defaultdict(int)
        for c in s:
            sc[c] += 1
        for c in t:
            tc[c] += 1
        
        return sc == tc