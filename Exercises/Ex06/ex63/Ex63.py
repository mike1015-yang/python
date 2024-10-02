class Cuboid:
    def __init__(self, length=1.0, width=1.0, height=1.0):
        self.length = length
        self.width = width
        self.height = height

    def volume(self):
        return self.length * self.width * self.height

    def getInfo(self):
        return f"長: {self.length}, 寬: {self.width}, 高: {self.height}, 體積: {self.volume()}"

    @staticmethod
    def getCuboidsInfo(cuboids):
        text = ""
        for cuboid in cuboids:
            text += cuboid.getInfo() + "\n"

        return text


class House(Cuboid):
    def __init__(self, length=1.0, width=1.0, height=1.0, material=""):
        super().__init__(length, width, height)
        self.material = material

    def getInfo(self):
        return f"{super().getInfo()}, 材質: {self.material}"


def main():
    num = int(input("請問有幾間房屋? "))
    houses = inputHouses(num)
    print(f"輸入的{num}間房屋資訊如下:")
    print(Cuboid.getCuboidsInfo(houses))


def inputHouses(num):
    houses = []
    for i in range(num):
        strList = input(f"請輸入第{i + 1}間房屋的長、寬、高與材質(空白間隔): ").split()
        house = House(float(strList[0]), float(strList[1]), float(strList[2]), strList[3])
        houses.append(house)

    return houses


main()
