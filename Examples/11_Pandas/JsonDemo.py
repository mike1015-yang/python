import pandas as pd


def main():
    # 讀取JSON文件
    dfJSON = pd.read_json("dataSource/books.json")
    print(f"dfJSON:\n{dfJSON}")
    print("-----------------------------------")

    # 轉存JSON文件，orient="records"產生的結果不會有index
    dfJSON.to_json("dataGen/df.json", orient="records")
    print("轉存JSON文件成功")


main()
