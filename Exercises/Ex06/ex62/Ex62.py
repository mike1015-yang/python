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

def main():
    num = int(input("請問有幾個長方體? "))
    cuboids = inputCuboids(num)
    print(f"輸入的{num}個長方體資訊如下:")
    print(Cuboid.getCuboidsInfo(cuboids))


def inputCuboids(num):
    cuboids = []
    for i in range(num):
        strList = input(f"請輸入第{i + 1}個長方體的長、寬、高(空白間隔): ").split()
        cuboid = Cuboid(float(strList[0]), float(strList[1]), float(strList[2]))
        cuboids.append(cuboid)

    return cuboids


main()