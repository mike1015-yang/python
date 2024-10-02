import re


def main():
    mobilePhone("0912345678")
    split("Python, 500, Paul")


# 利用正規表示式檢查手機號碼
def mobilePhone(number):
    # 使⽤「r""」raw string，可免除使⽤跳脫符號⿇煩
    # 要求格式為：開頭必須為09，後面接著為8個數字
    pattern = re.compile(r"09[0-9]{8}")
    # fullmatch()會比對整個字串；match()只會比對開始位置
    result = "是手機號碼" if pattern.fullmatch(number) else "不是手機號碼"
    print(f"{number} {result}")


# 利用正規表示式將分隔符號去掉
def split(text):
    pattern = re.compile(r"\s*,\s*")
    fields = pattern.split(text)
    print("資料分割後：")
    for f in fields:
        print(f)


main()
