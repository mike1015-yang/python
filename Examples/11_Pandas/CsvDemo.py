import pandas as pd


def main():
    # 讀取CSV文件，預設分隔符號為","，可使用正規表示式設定分隔符號
    # 建議設定engine="python"；因為預設為engine="c"，沒有支援正規表示式
    dfCSV = pd.read_csv("dataSource/books.csv", delimiter=r"\s*,\s*", engine="python")
    # 如果CSV內容沒有欄位列，加上header=None即可
    # dfCSV = pd.read_csv("dataSource/books.csv", delimiter=r"\s*,\s*", header=None, engine="python")
    print(f"dfCSV:\n{dfCSV}")
    print("-----------------------------------")

    # 轉存CSV文件，header=False不會有欄位名稱，index=False不會有index
    dfCSV.to_csv("dataGen/df.csv", header=False, index=False)
    print("轉存CSV文件成功")


main()
