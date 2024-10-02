# Logical - AND
money = 30000
day = 7
travel = money >= 100000 and day >= 10
if travel:
    print("可以去澳洲看黃金海岸")
else:
    print("只能在公園看黃金獵犬")

# Logical - OR
aircraft = False
boat = True
result = aircraft or boat
if result:
    result = "Yes"
else:
    result = "No"
print(f"是否成行: {result}")

# Logical - NOT
age = 19
adult = age >= 18
if not adult:
    print(f"{age} 歲不可進入觀賞")
else:
    print("歡迎觀賞")