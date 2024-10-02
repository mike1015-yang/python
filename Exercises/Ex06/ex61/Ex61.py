class Cuboid:
    def __init__(self, length=1.0, width=1.0, height=1.0):
        self.length = length
        self.width = width
        self.height = height

    def volume(self):
        return self.length * self.width * self.height

    def getInfo(self):
        return f"長: {self.length}, 寬: {self.width}, 高: {self.height}, 體積: {self.volume()}"

def main():
    strList = input("請輸入長方體的長、寬、高(空白間隔): ").split()
    cuboid = Cuboid(float(strList[0]), float(strList[1]), float(strList[2]))
    print("輸入的長方體資訊如下: ")
    print(cuboid.getInfo())

main()