class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for index, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                stack_t, stack_i = stack.pop()
                res[stack_i] = index - stack_i
            stack.append((temp, index))

        return res