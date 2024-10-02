# lambda指派
maximum = lambda num1, num2: num1 if num1 > num2 else num2
result = maximum(1, 2)
print(f"maximum: {result}")

# 傳遞lambda
def maxNumber(num1, num2, max):
    print(f"maximum: {max(num1, num2)}")

maxNumber(1, 2, lambda num1, num2: num1 if num1 > num2 else num2)
