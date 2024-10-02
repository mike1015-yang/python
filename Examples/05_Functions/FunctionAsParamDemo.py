# 函式型參數
def showDivide(divideFunc, num1, num2):
    quotient = divideFunc(num1, num2)
    print(f"{num1} / {num2} = {quotient}")

def myDivide(dividend, divisor):
    quotient = dividend / divisor
    return quotient

showDivide(myDivide, 10, 2)

## 常見的函式型參數應用
# 別人寫好的功能函式
def connect(task):
    print("開始連線...")
    print("連線成功，可以開始幫你做事!")
    task()
    print("任務完成")
    print("連線結束!")

#########################
## 我交付的任務內容
def myTask():
    print("任務內容: 傳送資料到server")

connect(myTask)