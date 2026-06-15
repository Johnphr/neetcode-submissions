class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        openParenthesis = ["(" for i in range(n)]
        closeParenthesis = [")" for i in range(n)]
        def backtrack(O, C):
            if not openParenthesis and not closeParenthesis:
                res.append("".join(stack))
                return
            
            if O:
                stack.append(O.pop())
                backtrack(O, C)
                stack.pop()
                O.append("(")
            
            if len(C) > len(O):
                stack.append(C.pop())
                backtrack(O, C)
                stack.pop()
                C.append(")")

        backtrack(openParenthesis, closeParenthesis)
        return res
            