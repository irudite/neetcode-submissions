class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                one = stack.pop()
                two = stack.pop()
                stack.append(two - one)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                one = stack.pop()
                two = stack.pop()
                stack.append(int(float(two) / one))
            else:
                stack.append(int(c))

        return stack[0]
