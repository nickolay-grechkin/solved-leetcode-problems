def isValid(s):
    stack = []
    parentheses = {"(":")", "{":"}", "[":"]"}
    
    for char in s:
        if char in parentheses:
            stack.append(char)
        if not stack or char != parentheses[stack.pop()]:
            return False
    
    return len(stack) == 0

