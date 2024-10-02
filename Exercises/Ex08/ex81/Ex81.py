def main():
    while True:
        try:
            dividend = int(input("輸入被除數(整數): "))
            divisor = int(input("輸入除數(整數): "))
            print(f"{dividend} ÷ {divisor} = {dividend // divisor} ... {dividend % divisor}")
            break
        except ValueError:
            print(f"被除數或除數格式錯誤，請重新輸入")
        except ZeroDivisionError:
            print(f"除數不可為0，請重新輸入")


main()
