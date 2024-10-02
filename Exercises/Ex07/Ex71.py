import math
import random


def prime(num):
    # 數字為1, 2, 3時for迴圈檢查不到，所以直接決定是否為質數
    if num == 1:
        return False
    if num == 2 or num == 3:
        return True
    for factor in range(2, int(math.sqrt(num) + 1)):
        if num % factor == 0:
            return False
    return True


def main():
    numbers = []
    count = int(input("使用亂數產生幾個 1～100 (不含) 整數？ "))
    while len(numbers) < count:
        number = random.randrange(1, 100)
        numbers.append(number)

    for num in numbers:
        print(num, end="")
        if prime(num):
            print(" 是質數")
        else:
            print(" 不是質數")


main()
