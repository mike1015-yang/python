# 基本類型、字串比對與or
rating = int(input('請輸入名次: '))
match rating:
    case 1:
        print(f"第{rating}名，10,000元獎金")
    case 2:
        print(f"第{rating}名，5,000元獎金")
    case 3:
        print(f"第{rating}名，2,000元獎金")
    # 可以使用as來取得對應值
    case (4 | 5) as number:
        print(f"佳作(第{number}名)，500元獎金")
    case _:
        print("還要再努力")

# Tuple比對
niceSeasons = ("spring", "autumn")
match niceSeasons:
    case ("summer", "winter"):
        print("冷熱分明季節")
    case ("spring", "autumn"):
        print("溫和季節")
    case _:
        print('比對錯誤')
