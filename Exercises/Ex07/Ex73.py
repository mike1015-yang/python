import re


def birthdayValid(birthday):
    # 1900~2020; 1,3,5,7,8,10,12大月日期可到31號; 4,6,9,11小月可到30號; 2月可到29號
    birthdayReg = r"(19[0-9]{2}|20[01][0-9]|2020)-" \
                  "(((0?[13578]|10|12)-(0?[1-9]|[12][0-9]|3[01]))|" \
                  "((0?[469]|11)-(0?[1-9]|[12][0-9]|30))|" \
                  "((0?2)-(0?[1-9]|[12][0-9])))"
    pattern = re.compile(birthdayReg)
    return pattern.fullmatch(birthday)


def ageValid(age):
    # 最大年紀119.99(吃到百二)
    # r - raw string，建議使用
    ageReg = r"(1[0-1][0-9]|[0-9]{1,2})(\.[0-9]{1,2})?"
    # 下列方式也可以
    # ageReg = "(1[0-1][0-9]|[0-9]{1,2})(\\.[0-9]{1,2})?"
    pattern = re.compile(ageReg)
    return pattern.fullmatch(age)


def main():
    while True:
        birthday = input("生日 (例如1981-1-1): ").strip()
        if birthdayValid(birthday):
            print(f"生日格式正確: {birthday}")
            break
        else:
            print("生日格式錯誤，請再輸入一次！")

    while True:
        age = input("年齡 (可以為小數): ").strip()
        if ageValid(age):
            print(f"年齡格式正確: {age}")
            break
        else:
            print("年齡格式錯誤，請再輸入一次！")


main()
