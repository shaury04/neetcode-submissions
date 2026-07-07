class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while True:
            num = numbers[l] + numbers[r]
            if num == target:
                return [l+1,r+1]
            elif num < target:
                l += 1
            else:
                r -= 1
        return [0,0]
