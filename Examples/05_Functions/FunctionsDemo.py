# 無參數、無回傳值
def sayHello():
    print("Hello")

sayHello()
print("--------------------------------------------")

# 2個參數，無回傳值
def showInfo(name, price):
    print(f"書名: {name}\n定價: {price}")

showInfo("Python", 500)
print("--------------------------------------------")

# 參數有預設值（default arguments）
# parameter: (定)參數，argument: (傳)引數
def showBookInfo(name, price, discount=0.2):
    info = f"書名: {name}\n售價: {price * (1 - discount)}"
    print(info)

# 呼叫時不傳值代表使用預設值
showBookInfo("Python", 500)
# 呼叫時也可傳值代表不使用預設值
showBookInfo("Python", 500, 0.3)
print("--------------------------------------------")

# 一個參數有預設值，其後的參數也必須有預設值，
# 否則產生 "non-default parameter follows default parameter" 錯誤
# def showBookInfo2(name, price=500, discount):
#     info = f"書名: {name}\n售價: {price * (1 - discount)}"
#     print(info)

# 2個參數與1個回傳值
# 可以不定義回傳類型
def getInfo(name, price):
    info = f"書名: {name}\n定價: {price}"
    return info

result = getInfo("Python", 500)
print(result)
print("--------------------------------------------")

# 也可定義回傳類型
def getInfo2(name, price) -> str:
    info = f"書名: {name}\n定價: {price}"
    return info

result = getInfo2("Python", 500)
print(result)
print("--------------------------------------------")

# 多個參數與多個回傳值 (其實是回傳tuple)
def getSaleInfo(name, price, discount):
    salePrice = price * (1 - discount)
    info = f"書名: {name}\n定價: {price}"
    return salePrice, info
# 使用索引取值
result = getSaleInfo("Python", 500, 0.2)
print(f"{result[1]}\n特價: {result[0]}")
# 使用變數取值
salePrice, info = getSaleInfo("Python", 500, 0.2)
print(f"info:\n{info}\nsalePrice: {salePrice}")
print("--------------------------------------------")

# 任意引數（arbitrary arguments），一個函式只能定義一個任意引數，否則錯誤
def showNames(*names, a):
    for name in names:
        print(name)
    print(f"共{len(names)}本書")

showNames("Python", "Java", "JS")
print("--------------------------------------------")

# keyword arguments，因為指定名稱，所以引數可以不按照參數順序
def showBook(name, price, discount):
    info = f"書名: {name}\n售價: {price * (1 - discount)}"
    print(info)

showBook(name="Python", discount=0.2, price=500)
print("--------------------------------------------")
