class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == '+':
                op1, op2 = stack.pop(), stack.pop()
                stack.append(op1 + op2)
            elif token == '-':
                op1, op2 = stack.pop(), stack.pop()
                stack.append(op2 - op1)
            elif token == '*':
                op1, op2 = stack.pop(), stack.pop()
                stack.append(op1 * op2)
            elif token == '/':
                op1, op2 = stack.pop(), stack.pop()
                stack.append(int(op2 / op1))
            else:
                stack.append(int(token))
        return stack[-1]