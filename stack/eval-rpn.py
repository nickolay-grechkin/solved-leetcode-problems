def evalRPN(tokens):
    if len(tokens) == 1:
        return tokens[0]
    
    stack = []
    operations = ['+', '-', '*', '/']

    def calculateResult(number1, number2, operation):
        match operation:
            case '+':
                return number1 + number2
            case '-':
                return number1 - number2
            case '*':
                return number1 * number2
            case '/':
                return int(number1 / number2)
    
    for i in tokens:
        if i not in operations:
            stack.append(i)
        else:
            number2 = stack.pop()
            number1 = stack.pop()
            stack.append(calculateResult(int(number1), int(number2), i))
    return stack.pop();
                

print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))