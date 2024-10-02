friends = {}
text = "可借錢的好友: "
count = 0

num = int(input("請問有幾個好友? "))
for i in range(num):
    friendInput = input(f"請輸入第{i + 1}個好友名與身上現金: ")
    friend = friendInput.split()
    name = friend[0]
    cash = int(friend[1])
    friends[name] = cash

print("--------------------------------------------------")

borrow = int(input("請輸入欲借現金: "))
for name, cash in friends.items():
    if borrow <= cash:
        count += 1
        text += name + ", "

text += f"共{count}人"
print(text)