import numpy as np
import pandas as pd


def createDataFrame():
    print("--createDataFrame()----------------")
    # 內容來自2維list：1維list長度可以不同，缺值則為NaN
    data1 = [["Python", 500], ["Java", 400], ["Swift"]]
    # columns是欄位標籤，預設為0, 1, 2...
    df0 = pd.DataFrame(data1)
    print(f"df:\n{df0}")
    print("-----------------------------------")
    # 可以指定欄位標籤
    df1 = pd.DataFrame(data1, columns=["name", "price"])
    print(f"df1:\n{df1}")
    print("-----------------------------------")
    # 取得DataFrame資訊
    print("df1.info(): ")
    df1.info()
    print("-----------------------------------")
    # 內容來自dict-list：list長度要相同，否則產生ValueError
    data2 = {"name": ["Python", "Java", "Swift"], "price": [500, 450, 550]}
    df2 = pd.DataFrame(data2)
    print(f"df2:\n{df2}")
    print("-----------------------------------")
    # 內容來自list-dict：dict長度可以不同，缺值則為NaN
    data3 = [{"name": "Python", "price": 500},
             {"name": "Java", "price": 450},
             {"name": "Swift"}]
    df3 = pd.DataFrame(data3)
    print(f"df3:\n{df3}")
    print("-----------------------------------")
    # 內容來自ndarray：長度要相同，否則產生ValueError
    data4 = np.array([["Python", 500], ["Java", 400], ["Swift", 550]])
    df4 = pd.DataFrame(data4)
    print(f"df4:\n{df4}")
    print("-----------------------------------")
    print(f"df1:\n{df1}")
    print("-----------------------------------")
    # DataFrame轉dict
    print(f"df1.to_dict():\n{df1.to_dict()}")
    print("-----------------------------------")
    # DataFrame轉ndarray
    print(f"df1.to_numpy():\n{df1.to_numpy()}")
    print("-----------------------------------")
    # DataFrame轉list，需要先轉成ndarray
    print(f"df1.to_numpy().tolist():\n{df1.to_numpy().tolist()}")
    print("-----------------------------------")


def main():
    createDataFrame()


main()
