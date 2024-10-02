import numpy as np


def main():
    # 1維陣列 #
    # (list轉array)
    print(f"np.array([1, 2, 3]): {np.array([1, 2, 3])}")
    print("-----------------------------------")
    # 呼叫arange()建立1~10(不含)且差值為1的1維陣列
    print(f"np.arange(1, 10, 1): {np.arange(1, 10, 1)}")
    print("-----------------------------------")

    # 2維陣列 #
    print(f"np.array([[1, 2, 3], [4, 5, 6]]):\n"
          f"{np.array([[1, 2, 3], [4, 5, 6]])}")
    print("-----------------------------------")
    # 建立2x3且初始值為0的整數2維陣列。不指定dtype則為float
    print(f"np.zeros((2, 3), dtype='int'):\n"
          f"{np.zeros((2, 3), dtype='int')}")
    print("-----------------------------------")
    # 建立2x3且初始值為空字串的2維陣列
    print(f"np.empty((2, 3), dtype='str'):\n"
          f"{np.empty((2, 3), dtype='str')}")
    print("-----------------------------------")


main()
