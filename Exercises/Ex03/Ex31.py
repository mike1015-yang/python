money = int(input("身上的錢: "))
day = int(input("放假天數: "))

if money >= 20000 and day >= 5:
    print("可以去泰國玩")
elif money >= 20000:
    print("有錢沒閒")
elif day >= 5:
    print("有閒沒錢")
else:
    print("沒錢沒閒，真可憐")