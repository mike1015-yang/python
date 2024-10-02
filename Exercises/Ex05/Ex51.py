def calculate(numbers):
    numSum = 0
    for num in numbers:
        numSum += num
    average = numSum / len(numbers)
    return numSum, average


def main():
    numList = []
    inputStr = input("請輸入整數數列(空白分隔): ")
    print(f"數列為: {inputStr}")
    strList = inputStr.split()
    for s in strList:
        numList.append(int(s))
    result = calculate(numList)
    print(f"總和 = {result[0]}")
    print(f"平均 = {result[1]}")


main()
