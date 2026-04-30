
def add(a, b):
    if type(a) not in (int, float) or type(b) not in (int, float):
        return "Error: Both a and b must be numbers"
    return a + b


def subtract(a, b):
    if type(a) not in (int, float) or type(b) not in (int, float):
        return "Error: Both a and b must be numbers"
    return a - b

def multiply(a, b):
    if type(a) not in (int, float) or type(b) not in (int, float):
        return "Error: Both a and b must be numbers"
    return a * b

def divide(a, b):
    if type(a) not in (int, float) or type(b) not in (int, float):
        return "Error: Both a and b must be numbers"
    if b==0:
        return "Error:  Can not divide by zero"
    return a / b


