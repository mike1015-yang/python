def calculate(numbers, myFunction):
    myFunction(numbers)


def main():
    numList = []
    inputStr = input("請輸入整數數列(空白分隔): ")
    print(f"數列為: {inputStr}")
    strList = inputStr.split()
    for s in strList:
        numList.append(int(s))

    def myAverage(numbers):
        numSum = 0
        for num in numbers:
            numSum += num
        print(f"平均 = {numSum / len(numbers)}")

    calculate(numList, myAverage)


main()
