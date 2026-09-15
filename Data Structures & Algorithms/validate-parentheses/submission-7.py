class Solution:
    def isValid(self, s: str) -> bool:
        close = {"}":"{", ")":"(", "]":"["}
        stack = []
        for c in s:
            if c in close:
                if not stack:
                    return False
                if stack.pop() != close[c]:
                    return False
            else:
                stack.append(c)
        if stack:
            return False
        return True