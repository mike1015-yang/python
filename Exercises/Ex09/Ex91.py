import os


def userInput():
    lines = ""
    print("輸入資料 (或直接按 Enter 結束): ")
    while True:
        line = input()
        # 空字串被視為False
        if line:
            lines += line + "\n"
        else:
            break

    return lines


def demoWrite(file, text):
    # "a" (append) 代表在已有的檔案內容附加文字
    with open(file, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print("存檔完畢!")


def main():
    # 存放目錄不存在就建立，相對路徑代表存放位置跟執行的Python檔案放在同一目錄
    writeDir = "write"
    if not os.path.isdir(writeDir):
        os.makedirs(writeDir)

    file = "write/memo.txt"
    demoWrite(file, userInput())


main()
