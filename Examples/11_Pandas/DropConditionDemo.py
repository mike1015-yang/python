import pandas as pd

# 移除錯誤資料
def dropCondition():
    df = pd.read_csv("dataSource/raw.csv", delimiter=",", engine="python", skipinitialspace=True)
    print(f"df:\n{df}")
    print()
    # 自訂錯誤條件當作移除依據
    # print("df.drop(df[df['price'] < 0].index):")
    # print(df.drop(df[df['price'] < 0].index))


    # 也可使用迴圈
    print("將「price < 0」的資料移除: ")
    for i in df.index:
        if df.loc[i, "price"] < 0:
            df.drop(i, inplace=True)
    print(f"df:\n{df}")

def main():
    dropCondition()
    

main()
