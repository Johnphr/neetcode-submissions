class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {"+", "-", "*", "/"}
        for token in tokens:
            if token in ops:
                match token:
                    case "+":
                        stack.append(stack.pop() + stack.pop())
                    case "-":
                        stack.append(-stack.pop() - -stack.pop())
                    case "*":
                        stack.append(stack.pop() * stack.pop())
                    case "/":
                        if stack[-2] == 0:
                            stack.pop()
                            stack.pop()
                            stack.append(0)
                        else:
                            stack.append(math.trunc(stack.pop() ** -1 / stack.pop() ** -1))
            else:
                stack.append(int(token))
        return stack[0]



        