class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ns = sorted(nums)
        res = []
        end = len(ns)
        for i in range(end - 2):
            if i > 0 and ns[i] == ns[i-1]:
                continue
            l, r = i + 1, end - 1
            while l < r:
                total = ns[i] + ns[l] + ns[r]
                if total == 0:
                    res.append([ns[i],ns[l],ns[r]])
                    while l < r and ns[l] == ns[l + 1]:
                        l += 1
                    l += 1
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1
        return res


