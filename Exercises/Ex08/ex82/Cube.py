class CubeError(BaseException):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"CubeError: {self.message}"


class Cube:
    def __init__(self, length):
        self.__length = 0.0
        self.length = length

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length):
        if length <= 0.0:
            raise CubeError(f"正立方體邊長不可為0或負數")
        else:
            self.__length = length

    def volume(self):
        return self.length ** 3

    def __str__(self):
        return f"邊長: {self.length}, 體積: {self.volume()}"
