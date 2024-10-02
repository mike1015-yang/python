import locale
import os

def demoRead(file):
    # "r"(read)代表讀資料，"t"(text)代表文字內容；預設為"rt"，如果讀取文字檔案可省略不寫
    # f - file object
    # with區塊結束會自動關閉file，所以不需要呼叫f.close()
    # encoding(文字編碼)不區別大小寫，如果不設定，會採用該平台的encoding
    with open(file, "rt", encoding="UTF-8") as f:
        for line in f:
            print(line, end="")

        print("\n相關資訊: ")
        print(f"f.name: {f.name}")
        print(f"f.closed(with內): {f.closed}")
        print(f"f.mode: {f.mode}")
        print(f"f.encoding: {f.encoding}")
        print(f"system encoding: {locale.getpreferredencoding()}")

    print(f"f.closed(with外): {f.closed}")


def demoWrite(file):
    text = "春暖花開"
    # "w" (write) 代表寫入資料，如果寫入文字檔案可省略 "t" (text)
    with open(file, "w", encoding="UTF-8") as f:
        f.write(text)
    print("儲存完畢!")


def demoAppend(file):
    text = "秋高氣爽\n"
    # "a" (append) 代表在已有的檔案內容附加文字
    with open(file, "a", encoding="UTF-8") as f:
        f.write(text)
    print("附加完畢!")


def main():
    readDir = "read"
    # 存放目錄不存在就建立，相對路徑代表存放位置跟執行的Python檔案放在同一目錄
    writeDir = "write"
    if not os.path.isdir(writeDir):
        os.makedirs(writeDir)

    print("---demoRead()------------")
    # 路徑是相對位置，要進入到此python檔案所在目錄執行
    demoRead(f"{readDir}/books.txt")
    print("---demoWrite()------------")
    demoWrite(f"{writeDir}/fileOut.txt")
    print("---demoAppend()------------")
    demoAppend(f"{writeDir}/fileAppend.txt")


main()