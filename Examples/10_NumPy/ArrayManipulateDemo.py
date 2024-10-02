import numpy as np


def main():
    a1 = np.array([1, 2, 3, 4, 5, 6])
    a2 = np.array(
        [[1, 2, 3], 
         [4, 5, 6], 
         [7, 8, 9]])
    print(f"a1: {a1}")
    print(f"a2:\n{a2}")
    print("-----------------------------------")

    # 取值 #
    print("1維陣列取值:")
    # 取索引為0的元素值
    print(f"a1[0]: {a1[0]}")
    # 取索引0到3(不含)的元素值
    print(f"a1[0:3]: {a1[0:3]}")
    print("2維陣列取值:")
    # 取列索引0到2(不含)，欄索引為1的元素值
    print(f"a2[0:2, 1]: {a2[0:2, 1]}")
    # 取列索引1到3(不含)，欄索引為1到3(不含)的元素值
    print(f"a2[1:3, 1:3]:\n{a2[1:3, 1:3]}")
    a2[1:2, 1:2] = 5
    # 取列索引1, 2，欄索引1, 2的元素值
    print(f"a2[(1, 2), (1, 2)]: {a2[(1, 2), (1, 2)]}")
    print("-----------------------------------")
    # 走訪1維陣列
    print("走訪1維陣列np.nditer(a1): ", end="")
    for number in np.nditer(a1):
        print(number, end=" ")
    print()
    # 走訪2維陣列
    print("走訪2維陣列np.nditer(a2): ", end="")
    for number in np.nditer(a2):
        print(number, end=" ")
    print()
    print("-----------------------------------")
    # 需要賦值才會改變原本的陣列
    print("1維陣列附加、新增、刪除(會產生新的陣列):")
    print(f"np.append(a1, 7): {np.append(a1, 7)}")
    print(f"np.insert(a1, 0, 8): {np.insert(a1, 0, 8)}")
    print(f"np.delete(a1, 0): {np.delete(a1, 0)}")

    print("下面2種方式為取出陣列局部，仍會參照到原始陣列:")
    print(f"a1[slice(0, 3)]: {a1[slice(0, 3)]}")
    print(f"a1[0:3]: {a1[0:3]}")

    print("2維陣列附加、新增、刪除:")
    arr_1d = np.array([10, 11, 12])
    print(f"arr_1d: {arr_1d}")
    print("axis=0代表列, axis=1代表欄，未指定axis會將array平面化看待，所以值為arr_1d, [arr_1d]結果一樣")
    print(f"np.append(a2, arr_1d):\n{np.append(a2, arr_1d)}")
    print(f"np.append(a2, [arr_1d]):\n{np.append(a2, [arr_1d])}")

    # 指定axis=0, 代表要新增列
    print("append()直接附加其後，所以需要附加2維資料: [arr_1d]")
    # append: 維度要一樣才行，arr_1d是一維，所以要加[arr_1d]
    print(f"np.append(a2, [arr_1d], axis=0):\n{np.append(a2, [arr_1d], axis=0)}")
    print("insert()有指定是哪一列，所以新增1維資料: arr_1d")
    print(f"np.insert(a2, 1, arr_1d, axis=0):\n{np.insert(a2, 1, arr_1d, axis=0)}")

    # 指定axis=1, 代表要新增欄[[10], [11], [12]]
    print("append()直接附加其後，所以需要附加2維資料: [[10], [11], [12]]，否則產生ValueError")
    print(f"np.append(a2, [[10], [11], [12]], axis=1):\n{np.append(a2, [[10],  [11], [12]], axis=1)}")
    print("不可直接附加[arr_1d]，先呼叫transpose()處理[arr_1d]，之後方可附加在最後一欄")
    print(f"np.transpose([arr_1d]):\n{np.transpose([arr_1d])}")
    print(f"np.append(a2, np.transpose([arr_1d]), axis=1):\n{np.append(a2, np.transpose([arr_1d]), axis=1)}")

    print("insert()有指定是哪一欄，所以新增1維資料: [10, 11, 12]")
    print(f"np.insert(a2, 1, [10, 11, 12], axis=1):\n{np.insert(a2, 1, [10, 11, 12], axis=1)}")

    print(f"np.delete(a2, 0, axis=0):\n{np.delete(a2, 0, axis=0)}")
    print(f"np.delete(a2, 0, axis=1):\n{np.delete(a2, 0, axis=1)}")
    print("-----------------------------------")

    # 重構內容(會產生新的陣列)
    print("1維陣列重構維度:")
    b = a1.reshape(2, 3)
    print(f"b = a1.reshape(2, 3):\n{b}")
    print("將2維陣列展開:")
    print(f"b.ravel(): {b.ravel()}")
    print("2維陣列的列與欄位置轉換:")
    print(f"np.transpose(b):\n{np.transpose(b)}")
    print("-----------------------------------")

main()
