import pandas as pd

# 轉換成日期時間格式
def toDatetime():
    df = pd.read_csv("dataSource/raw.csv", delimiter=",", engine="python", skipinitialspace=True)
    print(f"df:\n{df}")
    print()
    try:
        # "ISO8601"是標準的日期時間的表示法
        df['date'] = pd.to_datetime(df["date"], format="ISO8601")
        print(f"pd.to_datetime(df['date']):\n{df}")
    except Exception as err:
        print(f"Exception: {err}")


def main():
    toDatetime()


main()
