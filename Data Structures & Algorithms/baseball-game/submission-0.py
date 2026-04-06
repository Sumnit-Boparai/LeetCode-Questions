class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        res = 0
        for operation in operations:
            if operation == '+':
                res += (stack[-1] + stack[-2])
                stack.append(stack[-1] + stack[-2])
            elif operation == 'D':
                res += (stack[-1] * 2)
                stack.append(stack[-1] * 2)
            elif operation == 'C':
                res -= stack.pop()
            else:
                res += int(operation)
                stack.append(int(operation))

        return res