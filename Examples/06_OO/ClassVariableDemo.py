class Book:
    # 類別變數
    count = 0

    # 類別方法, @: annotation(註記)
    @classmethod
    def showCount(cls):
        print(f"count: {cls.count}")

    # name, price, author為實例變數，屬於各個物件所有
    def __init__(self, name="", price=0.0, author=""):
        Book.count += 1
        self.name = name
        self.price = price
        self.author = author

    def show(self):
        print(f"name: {self.name}")
        print(f"price: {self.price}")
        print(f"author: {self.author}")


Book.showCount()
print("-----------------------")
book1 = Book("Python", 500, "Paul")
book1.show()
print("-----------------------")
book2 = Book("C++", 400, "Cindy")
book2.show()
print("-----------------------")
Book.showCount()