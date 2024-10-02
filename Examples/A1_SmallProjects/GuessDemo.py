import random

# 第一次顯示給使用者看的主菜單
dishesMain = [
    "東坡肉", "糖醋鯉魚", "宋嫂魚羹", "三杯雞", "紅燒獅子頭",
    "梅菜扣肉", "叫花雞", "老皮嫩肉", "魚香茄子", "海南雞飯",
    "月亮蝦餅", "蔥爆牛肉", "番茄炒蛋", "鳳梨蝦球", "萬巒豬腳",
    "菜脯蛋"
]

# 備用菜單
dishesSwap = [
    "清蒸檸檬魚", "打拋豬肉", "咖哩牛肉", "泰式酸辣湯", "椒麻雞",
    "三杯中卷", "薑母鴨", "客家小炒", "薑絲大腸", "糖醋排骨",
    "麻婆豆腐", "宮保雞丁", "五更腸旺", "鹹蛋苦瓜", "燒酒雞",
    "蔭豉鮮蚵"
]


def show(dishes):
    print()
    count = 0
    text = ""
    for dish in dishes:
        text += f"{dish}   \t"
        count += 1
        # 每列印4道菜名就換行
        if count % 4 == 0:
            text += "\n"

    print(text)


def question(text):
    while True:
        answer = input(text)
        # 如果輸入的不是"y"或"n"，代表輸入錯誤 (轉成小寫再比對，代表不區別大小寫)
        if (not answer.lower() == "y") and (not answer.lower() == "n"):
            print("輸入錯誤，請再輸入一次")
            continue

        print("=================================================", end="")
        return answer.lower() == "y"


def guess(listMain, listSwap):
    length = len(listMain)
    while length > 1:
        # 將原listMain分兩半
        half = length // 2
        list01 = listMain[0:half]
        list02 = listMain[half:length]
        # 使用listSwap補足剩餘數量，補之前先隨機重排，讓使用者難抓規則
        random.shuffle(listSwap)
        # listShow = 主菜單 + 備用菜單
        # 如果half為8，則16-8=8代表要補8道菜；若為4則16-4=12代表要補12道菜
        listShow = list01 + listSwap[0:len(listSwap) - half]
        # 顯示前隨機重排，讓使用者難抓規則
        random.shuffle(listShow)
        show(listShow)

        yes = question("上列有你的最愛嗎？有按[y]，沒有按[n]: ")

        # 按[y]代表使用者最愛在list01，按[n]代表在list02
        listMain = list01 if yes else list02
        # 當half為1代表只剩下一道菜，必定為使用者最愛，可以列出該名稱並停止迴圈
        if half == 1:
            text = f"\n「{listMain[0]}」 是你的最愛"
            print(text)
            break

        # 已經剔除掉一半，只需在剩下的一半找出使用者最愛
        length = half


def main():
    # 顯示前隨機重排，讓使用者難抓規則
    random.shuffle(dishesMain)
    show(dishesMain)
    print("上列佳餚，請默記你的最愛。噓！不要說出來～ 只要誠實回答個幾次，我能猜出你的最愛！")
    start = question("開始請按[y]，結束請按[n]: ")
    if start:
        guess(dishesMain, dishesSwap)
    else:
        print("\n掰掰囉！")


main()
