from Cube import Cube, CubeError


def main():
    while True:
        try:
            length = float(input("立方體邊長: "))
            cube = Cube(length)
            print(cube)
            break
        except ValueError:
            print("數字格式不正確，請重新輸入")
        except CubeError as err:
            print(f"{err}，請重新輸入")

main()
