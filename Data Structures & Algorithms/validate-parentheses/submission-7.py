class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return False
        stack = []
        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            elif (c == ")" and not stack) or (c == "}" and not stack) or (c == "]" and not stack):
                return False
            elif c == ")":
                if stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            elif c == "}":
                if stack[-1] == "{":
                    stack.pop()
                else:
                    return False 
            elif c == "]":
                if stack[-1] == "[":
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False
            

