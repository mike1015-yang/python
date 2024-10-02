# 建立list以儲存數列
numList = []
# 取得使用者輸入的數列
inputStr = input("請輸入整數數列(空白分隔): ")
print(f"數列為: {inputStr}")
# 將數列切割，會儲存成str類型list
strList = inputStr.split()
# 將文字型數列轉成整數型數列
for s in strList:
    numList.append(int(s))

# 或簡化成下列寫法
# numList = list(map(int, input("請輸入整數數列(空白分隔): ").split()))

numList_sum = 0
for num in numList:
    numList_sum += num

numList_average = numList_sum / len(numList)
print(f"總和 = {numList_sum}")
print(f"平均 = {numList_average}")
