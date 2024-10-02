def recursive(count):
    if count > 0:
        print(count, end=" ")
        recursive(count - 1)


def loop(count):
    for number in range(count, 0, -1):
        print(number, end=" ")


def main():
    count = 10
    # 遞迴函式
    recursive(count)
    print()
    # 迴圈
    loop(count)
    print()


main()
