import pandas as pd

# 移除預設空值
def dropNa():
    # 原始資料如果沒有值，讀進來會轉成NaN
    # "skipinitialspace=True"代表忽略原始空白字元
    df = pd.read_csv("dataSource/raw.csv", delimiter=",", engine="python", skipinitialspace=True)
    print(f"df:\n{df}")
    print()

    # 先檢查哪些資料被視為空值
    print(f"df.isna():\n{df.isna()}")
    print()
    # 刪除帶有空值的該列資料
    print(f"df.dropna():\n{df.dropna()}")
    print("-----------------------------------")

# 移除自訂空值
def dropNaCustom():
    # 自訂哪些值視為空值
    naCustom = ["na", "--"]
    print(f"naCustom = {naCustom}")

    df = pd.read_csv("dataSource/raw.csv", na_values=naCustom, delimiter=",", engine="python", skipinitialspace=True)
    print(f"df:\n{df}")
    print()
    print(f"df.dropna():\n{df.dropna()}")
    print("-----------------------------------")


def main():
    dropNa()
    dropNaCustom()

 
main()
