SUM='sum'
SUB='sub'
DIV='div'
MULT='mult'

def calc(num1: int|float,num2: int|float,op: str):
    if op==SUM:
        return num1+num2
    elif op==SUB:
        return num1-num2
    elif op==MULT:
        return num1*num2
    elif op==DIV:
        return num1/num2 if num2!=0 else None
    else: 
        return "incorrect input"