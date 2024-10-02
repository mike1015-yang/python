import pandas as pd

# 填補空值
def fillNa():
    df = pd.read_csv("dataSource/raw.csv", delimiter=",", engine="python", skipinitialspace=True)
    print(f"df:\n{df}")
    print()
    print("將price欄位內的空值填入0")
    df["author"] = df["price"].fillna(0)
    print(f"df:\n{df}")


def main():
    fillNa()
    

main()
