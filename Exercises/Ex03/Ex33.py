start = int(input("起始值: "))
end = int(input("終止值: "))
text = ""
total = 0
count = 0

for number in range(start, end + 1):
    total += number
    count += 1
    if number < 10:
        text += "0"
    text += f"{number} "

    if count % 10 == 0:
        text += "\n"

text += f"\n總和: {total}"
print(text)
