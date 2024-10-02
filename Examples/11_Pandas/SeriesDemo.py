import numpy as np
import pandas as pd


def main():
    # Series內容可以來自list
    # pd.Series()的「Series()」是呼叫建構式而非一般函式
    seriesList = pd.Series(["Python", "Java", "JS", "Swift", "C#"], dtype='string')
    print(f"seriesList:\n{seriesList}")
    print("-----------------------------------")
    # 取index=0的值
    print(f"seriesList[0]: {seriesList[0]}")
    print("-----------------------------------")
    # 取index=[0]的series
    print(f"pd.Series(seriesList, index=[0]):\n"
          f"{pd.Series(seriesList, index=[0])}")
    print("-----------------------------------")
    # 取index=[0, 1]的series
    print(f"pd.Series(seriesList, index=[0, 1]):\n"
          f"{pd.Series(seriesList, index=[0, 1])}")
    print("-----------------------------------")

    # series可以來自dictionary
    seriesDic = pd.Series({
        "name": "Python",
        "price": 500,
        "author": "Paul"
    })
    print(f"seriesDic:\n{seriesDic}")
    print("-----------------------------------")
    # 取index=['name', 'price']的series
    print(f"pd.Series(seriesDic, index=['name', 'price']):\n"
          f"{pd.Series(seriesDic, index=['name', 'price'])}")
    print("-----------------------------------")

    # series可以來自NumPy的ndarray
    array = np.array(["Python", "Java", "JS", "Swift", "C#"])
    seriesArray = pd.Series(array)
    print(f"seriesArray:\n{seriesArray}")
    print("-----------------------------------")

    # series轉list
    print(f"seriesDic.tolist(): {seriesDic.tolist()}")
    print("-----------------------------------")
    # series轉dictionary
    print(f"seriesDic.to_dict(): {seriesDic.to_dict()}")
    print("-----------------------------------")
    # series轉ndarray
    print(f"seriesDic.to_numpy(): {seriesDic.to_numpy()}")
    print("-----------------------------------")


main()
