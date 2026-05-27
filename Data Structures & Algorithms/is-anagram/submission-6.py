class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sets, sett = Counter(), Counter()
        for i in range(len(s)):
            sets[s[i]] += 1
            sett[t[i]] += 1
        return sets == sett
