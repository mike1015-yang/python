score = int(input('請輸入分數: '))
text = f"{score}分，"
text1 = "贏得10,000元獎學金！\n"
text2 = "再努力！\n"
# conditional expression
text += text1 if score >= 85 else text2

print(text)
