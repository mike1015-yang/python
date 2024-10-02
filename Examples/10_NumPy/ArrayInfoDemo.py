import numpy as np


def main():
    a1 = np.array([1, 2, 3])
    print(f"a1: {a1}")
    print("-----------------------------------")
    a2 = np.array([
        [1, 2, 3], 
        [4, 5, 6]])
    print(f"a2:\n{a2}")
    print("-----------------------------------")
    # 取得維度資訊
    print(f"a1.ndim: {a1.ndim}, a1.shape: {a1.shape}")
    print(f"a2.ndim: {a2.ndim}, a2.shape: {a2.shape}")
    print("-----------------------------------")
    # size取得元素總個數，dtype取得型別
    print(f"a1.size: {a1.size}, a1.dtype: {a1.dtype}")
    print(f"a2.size: {a2.size}, a2.dtype: {a2.dtype}")
    print("-----------------------------------")


main()
