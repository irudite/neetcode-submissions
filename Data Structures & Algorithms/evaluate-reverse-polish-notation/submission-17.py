class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t == "+":
                stack.append(stack.pop() + stack.pop())
            elif t == "-":
                one = stack.pop()
                two = stack.pop()
                stack.append(two - one)
            elif t == "*":
                stack.append(stack.pop() * stack.pop())
            elif t =="/":
                one = stack.pop()
                two = stack.pop()
                stack.append(int(float(two)/ one))
            else:
                stack.append(int(t))

        return stack[0] 