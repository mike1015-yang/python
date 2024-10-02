# 函式型回傳值
def math(isAdd):
    return add if isAdd else subtract

def add(num1, num2):
    return f"{num1} + {num2} = {num1 + num2}"

def subtract(num1, num2):
    return f"{num1} - {num2} = {num1 - num2}"

calculate = math(isAdd=True)
result = calculate(5, 3)
print(result)