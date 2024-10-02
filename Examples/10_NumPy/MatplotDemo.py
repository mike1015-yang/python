# install numpy
import numpy as np
# install matplotlib
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


def lineBarChart():
    # 不支援中文字型，搜尋並下載「Noto Fonts TC」，解壓縮後隨意複製一個文字檔案到專案內
    # 建立FontProperties物件指定字型檔案名稱
    font = FontProperties(fname="NotoSansTC-Regular.otf")
    # fontproperties參數指定FontProperties物件
    plt.title("商品銷售量", fontproperties=font)
    plt.xlabel("2023年", fontproperties=font)
    plt.ylabel("銷售量", fontproperties=font)
    # x與y軸的值可能有中文，需要設定字型
    plt.xticks(fontproperties=font)
    plt.yticks(fontproperties=font)
    # 設定圖例在最佳位置
    plt.legend(loc="best")
    # 加網格
    plt.grid()

    # 資料設定
    months = np.array(["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"])
    productA = np.array([1000, 1200, 1350, 1250, 1330, 1240, 1150, 1250, 1230, 1300, 1320, 1400])
    productB = np.array([300, 320, 350, 315, 330, 340, 312, 325, 330, 323, 335, 340])

    # line chart
    # x軸, y軸, 標記, 線條顏色, 資料點樣式
    # plt.plot(months, productA, label="A", color="orange", marker=".")
    # # 再繪製一條線
    # plt.plot(months, productB, label="B", color="blue", marker="o")

    # bar chart
    plt.bar(months, productA, label="A", color="orange")
    plt.bar(months, productB, label="B", color="blue")

    # horizontal bar chart
    # plt.xlabel("銷售量", fontproperties=font)
    # plt.ylabel("2023年", fontproperties=font)
    # plt.barh(months, productA, label="A", color="orange")
    # plt.barh(months, productB, label="B", color="blue")

    # 將繪圖結果顯示
    plt.show()

def pieChart():
    font = FontProperties(fname="NotoSansTC-Regular.otf")
    plt.title("商品月銷售量", fontproperties=font)
    plt.xlabel("7月", fontproperties=font)
    # pie chart資料
    sales = [1000, 250, 200, 150, 100]
    labels = ["商品A", "商品B", "商品C", "商品D", "商品E"]
    # 顏色
    colors = ["red", "cyan", "green", "yellow", "orange"]

    # pie chart
    # autopct：值以百分比顯示
    # startangle：第一個資料起始度數，0度代表從x軸開始(3點鐘方向)，正度數代表逆時鐘
    # wedgeprops={"width": 0.6}：設定資料圓形佔比，0.6代表佔60%，內圓則佔40%
    # textprops={"fontproperties": font}：中文需要設定字型屬性
    plt.pie(
        sales, 
        labels=labels, 
        colors=colors, 
        # 兩個%: 類似像跳脫字元
        autopct='%.2f%%', 
        startangle=90, 
        wedgeprops={"width": 0.6}, 
        textprops={"fontproperties": font}
    )
    plt.show()

def main():
    lineBarChart()
    # pieChart()


main()
