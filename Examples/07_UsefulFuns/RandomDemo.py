import random

# 產生一個1~49(含)的整數亂數
print(f"random.randint(1, 49): {random.randint(1, 49)}")
# 產生一個1~49(不含)的整數亂數
print(f"random.randrange(1, 49): {random.randrange(1, 49)}")
# 產生一個2~49(不含)的偶數亂數
print(f"random.randrange(2, 49, 2): {random.randrange(2, 49, 2)}")
# 產生一個1~49(含)的浮點亂數
print(f"random.uniform(1, 49): {random.uniform(1, 49)}")

# 集合類型亂數
books = ["Python", "C++", "Java", "SQL"]
# 隨意挑出一個元素
print(f"random.choice(books): {random.choice(books)}")
# 洗牌(隨機重排)
random.shuffle(books)
print(f"random.shuffle(books): {books}")
