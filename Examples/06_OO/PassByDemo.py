number1 = 500.0
# 傳值

number2 = number1
number2 *= 0.8
print(id(number1))
print(id(number2))
print(f"number1 = {number1}")
print(f"number2 = {number2}")


class Book:
    def __init__(self, price=0.0):
        self.price = price


book1 = Book()
book1.price = 500.0
# 傳參照
book2 = book1
print(id(book1.price))
print(id(book2.price))
book2.price *= 0.8
print(f"book1.price = {book1.price}")
print(f"book2.price = {book2.price}")
