# 函式指派
def divide(dividend, divisor):
    quotient = dividend / divisor
    return quotient

mathDivide = divide
result = mathDivide(10, 2)
print(f"mathDivide(10, 2): {result}")