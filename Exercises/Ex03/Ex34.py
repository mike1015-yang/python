count = 0
text = ""
unluck = 4

while True:
    unluck = int(input("不吉利數字 (1 ~ 9) : "))
    if unluck < 1 or unluck > 9:
        print("輸入錯誤，請再輸入一次")
        continue
    else:
        break


for number in range(1, 49 + 1):
    if number // 10 == unluck or number % 10 == unluck:
        continue
    count += 1
    if number < 10:
        text += "0"
    text += f"{number} "

    if count % 10 == 0:
        text += "\n"

text += f"\n總個數: {count}"
print(text)
