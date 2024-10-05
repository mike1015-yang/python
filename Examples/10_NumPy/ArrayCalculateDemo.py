import numpy as np


def arrayMath():
    print("--arrayMath()------------------")
    a1 = np.array([4, 5, 6])
    a2 = np.array([1, 2, 3])
    print(f"a1: {a1}")
    print(f"a2: {a2}")
    print(f"np.add(a1, a2): {np.add(a1, a2)}")
    print(f"np.subtract(a1, a2): {np.subtract(a1, a2)}")
    print(f"np.multiply(a1, a2): {np.multiply(a1, a2)}")
    print(f"np.power(a1, a2): {np.power(a1, a2)}")
    print(f"np.divide(a1, a2): {np.divide(a1, a2)}")
    print(f"np.mod(a1, a2): {np.mod(a1, a2)}")
    print("-----------------------------------")


def arraySortStatistic():
    print("--arraySortStatistic()------------------")
    a = np.array(
        [[3, 11, 9], 
         [5, 2, 15], 
         [1, 6, 99]])
    print(f"a:\n{a}")
    print("-----------------------------------")
    # axis=0代表列, axis=1代表欄
    # 沿著axis 0排序
    print(f"np.sort(a, axis=0):\n{np.sort(a, axis=0)}")
    # 沿著axis 1排序
    print(f"np.sort(a, axis=1):\n{np.sort(a, axis=1)}")
    print("-----------------------------------")
    print(f"a:\n{a}")
    print("-----------------------------------")
    # 陣列所有值中的最小值，未指定axis會將array平面化看待
    print(f"np.amin(a): {np.amin(a)}")
    # 沿著axis 0取最小值
    print(f"np.amin(a, axis=0): {np.amin(a, axis=0)}")
    # 沿著axis 1取最小值
    print(f"np.amin(a, axis=1): {np.amin(a, axis=1)}")
    # 沿著axis 0取最大值
    print(f"np.amax(a, axis=0): {np.amax(a, axis=0)}")
    # 沿著axis 0取最大與最小的差值
    print(f"np.ptp(a, axis=0): {np.ptp(a, axis=0)}")
    # 沿著axis 0取總和
    print(f"np.sum(a, axis=0): {np.sum(a, axis=0)}")
    # 沿著axis 0取平均值
    print(f"np.mean(a, axis=0): {np.mean(a, axis=0)}")
    # average()也是算平均值，沒有加權則與mean()相同
    print(f"np.average(a, axis=0): {np.average(a, axis=0)}")
    # weights: 權重
    print(f"np.average(a, axis=0, weights=[1, 2, 3]): "
          f"{np.average(a, axis=0, weights=[1, 2, 3])}")
    # 沿著axis 0取中位數
    print(f"np.median(a, axis=0): {np.median(a, axis=0)}")
    # 沿著axis 0取百分位數，第50分位數就是中位數
    print(f"np.percentile(a, 50, axis=0): {np.percentile(a, 50, axis=0)}")

    # 變異數(方差): 數列內每個數字與其平均值之差的平方的平均
    print(f"np.var([1, 2, 30]): {np.var([1, 2, 30])}")
    # 標準差(變異數的平方根): 測量一組數值的離散程度
    print(f"np.std([1, 2, 30]): {np.std([1, 2, 30])}")
    print("-----------------------------------")


def main():
    arrayMath()
    arraySortStatistic()


main()