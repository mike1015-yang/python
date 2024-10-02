score = int(input('請輸入分數: '))
text = f"{score}分，"
# nested if-else statement
if score >= 75:
    if score >= 85:
        text += "贏得10,000元獎學金！\n"
    else:
        text += "贏得5,000元獎學金！\n"
else:
    text += "再努力！\n"

print(text)