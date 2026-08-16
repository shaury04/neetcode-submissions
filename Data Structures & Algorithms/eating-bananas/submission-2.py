class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            m = (l + r) // 2
            count = 0
            for p in piles:
                count += math.ceil(float(p) / m)
            if count > h:
                    l = m + 1
            else:
                res = min(m, res)
                r = m - 1
        return res
