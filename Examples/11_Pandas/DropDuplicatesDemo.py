import pandas as pd

# 移除重複資料
def dropDuplicates():
    df = pd.read_csv("dataSource/raw.csv", delimiter=",", engine="python", skipinitialspace=True)
    print(f"df:\n{df}")
    print()

    # 檢查是否有重複資料
    print(f"df.duplicated():\n{df.duplicated()}")
    # subset參數可以設定哪些欄位值相同就直接視為重複資料
    # print(f"df.duplicated(subset=['name']):\n{df.duplicated(subset=["name"])}")
    print()

    # 移除重複資料(所有欄位值相同才會被視為重複資料)
    print(f"df.drop_duplicates():\n{df.drop_duplicates()}")
    print()

    # subset參數可設定哪些欄位值相同就直接視為重複資料，可節省比對時間
    print("df.drop_duplicates(subset=['name']):")
    print(df.drop_duplicates(subset=["name"]))


def main():
    dropDuplicates()


main()
