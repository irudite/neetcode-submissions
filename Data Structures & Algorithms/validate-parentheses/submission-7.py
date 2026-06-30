class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {"}":"{", "]":"[", ")":"("}
        stack = []

        for c in s:
            if stack and c in mapping:
                if mapping[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        if not stack:
            return True
        
        return False