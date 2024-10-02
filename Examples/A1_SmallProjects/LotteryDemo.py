import random
import time


# 將使用者輸入的自選號轉成整數list並回傳
def inputNumbers(count):
    numbers = []
    # 將輸入的數列拆解成整數後存入numbers
    strings = input(f"請選號(最多 {count} 個，而且空白區隔): ").split()
    for string in strings:
        numbers.append(int(string))
    return numbers


# 依照數量產生一組號碼
def genNumbers(numbers, count):
    numbers = set(numbers)
    while len(numbers) < count:
        # 隨機產生一個1~49(含)的號碼
        randomNumber = random.randint(1, 49)
        numbers.add(randomNumber)
    return list(numbers)


# 檢查是否有中獎
def win(lotteryNumbers, special, userNumbers):
    matchSpecial = False
    winNumbers = []
    for userNum in userNumbers:
        # 如果已經出現特別號就不用比對
        # 如果還沒出現特別號，就比對是否符合特別號；如果是就continue不用再跟其他非特別號比對
        # 因為一個號碼不可能既是特別號又是其他中獎號碼
        if not matchSpecial and userNum == special:
            matchSpecial = True
            continue
        # 檢查是否為中獎號碼
        if userNum in lotteryNumbers:
            winNumbers.append(userNum)
            
    # 確定中獎號碼個數
    winNumbersLen = len(winNumbers)
    if winNumbersLen != 0:
        result = f"中 {winNumbers} 共 {winNumbersLen} 個號碼"
        if matchSpecial:
            result += f" + 特別號 {special}"
        print(result)
    else:
        if matchSpecial:
            print(f"只中特別號 {special}")
    # 確定獎次(大樂透玩法: https://www.taiwanlottery.com.tw/Lotto649/index.asp)
    if winNumbersLen == 6:
        print("恭喜中 頭獎")
    elif winNumbersLen == 5 and matchSpecial:
        print("恭喜中 貳獎")
    elif winNumbersLen == 5:
        print("恭喜中 參獎")
    elif winNumbersLen == 4 and matchSpecial:
        print("恭喜中 肆獎")
    elif winNumbersLen == 4:
        print("恭喜中 伍獎")
    elif winNumbersLen == 3 and matchSpecial:
        print("恭喜中 陸獎")
    elif winNumbersLen == 2 and matchSpecial:
        print("恭喜中 柒獎")
    elif winNumbersLen == 3:
        print("恭喜中 普獎")
    else:
        print("這次沒中獎，下次會更好")


def printSorted(numbers):
    print("排序後顯示: ")
    numbers.sort()
    for num in numbers:
        print(num, end=" ")


def main():
    ##########################################################
    ## 選號
    # 大樂透，使用者可以選6個號碼
    count = 6
    # 建立數列以儲存使用者的選號
    numbers = inputNumbers(count)
    numbersLen = len(numbers)
    # 自選號超過6個
    if numbersLen > count:
        # userNumbers儲存著使用者欲下注的號碼
        userNumbers = numbers[0:count]
        print(f"超過 {count} 個號碼，自動取前 {count} 個")
    # 自選號剛好6個
    elif numbersLen == count:
        userNumbers = numbers
    # 自選號少於6個
    else:
        userNumbers = genNumbers(numbers, count)
        print(f"自動產生 {count - len(numbers)} 個號碼")

    printSorted(userNumbers)
    print()
    print("-" * 30)
    ##########################################################
    ## 開獎
    print("開獎，大樂透號碼為: ")
    # 暫停2秒
    time.sleep(2)
    # 大樂透號碼總共有6個號碼加1個特別號
    lotteryCount = 6 + 1
    lotteryNumbers = genNumbers([], lotteryCount)
    # 自行指定中獎號碼
    # lotteryNumbers = [1, 2, 3, 4, 5, 6, 7]
    # 將最後一個號碼取出當作特別號碼
    special = lotteryNumbers.pop()

    for number in lotteryNumbers:
        print(number, end=" ")
    print(f"特別號: {special}")
    printSorted(lotteryNumbers)
    print(f"特別號: {special}")
    print("-" * 30)
    ##########################################################
    ## 對獎
    # 暫停2秒
    time.sleep(2)
    # 呼叫對獎函式
    win(lotteryNumbers, special, userNumbers)
    print("-" * 30)


main()
