class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ['+', '-', '*', '/']

        stack = []
        for token in tokens:
            if token in ops:
                arg2 = int(stack.pop())
                arg1 = int(stack.pop())
                result = 0
                match token:
                    case '+':
                        result = arg1 + arg2
                    case '-':
                        result = arg1 - arg2
                    case '*':
                        result = arg1 * arg2
                    case '/':
                        result = arg1 / arg2
                stack.append(result)
            else:
                stack.append(token)        
        return int(stack.pop())