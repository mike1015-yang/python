import random

lotterySet = set()
# 大樂透號碼總共有6個號碼加1個特別號
lotteryCount = 6 + 1
while len(lotterySet) < lotteryCount:
    # 隨機產生一個1~49的號碼
    number = random.randint(1, 49)
    lotterySet.add(number)

# set轉成list方便移除指定元素與排序
lotteryList = list(lotterySet)
# 將最後一個號碼取出當作特別號碼
special = lotteryList.pop()
print("開獎，大樂透號碼為: ")
for number in lotteryList:
    print(number, end=" ")
print(f"特別號: {special}")

# 排序
lotteryList.sort()
print("由小到大排列:")
for number in lotteryList:
    print(number, end=" ")
print(f"特別號: {special}")
