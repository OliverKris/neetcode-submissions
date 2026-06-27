class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {
            ')' : '(',
            ']' : '[',
            '}' : '{',
        }
        stack = []
        
        for char in s:
            if char in parentheses:
                if stack == []:
                    return False
                top = stack.pop()
                if parentheses.get(char) != top:
                    return False
            else:
                stack.append(char)
        return stack == []