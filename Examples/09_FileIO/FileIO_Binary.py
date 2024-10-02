import os


def demoReadWriteBinary(source, destination):
    with open(source, "rb") as fs, open(destination, "wb") as fd:
        # 沒有引數代表讀取整個檔案內容
        content = fs.read()
        # 將整個內容存檔，會回傳寫入大小(byte)
        size = fd.write(content)
        print(f"file size: {size}")


def demoReadWriteLarge(source, destination):
    # 檔案過大建議訂定讀入並暫存的資料量(byte)
    chunk_size = 1024
    with open(source, "rb") as fs, open(destination, "wb") as fd:
        while True:
            chunk = fs.read(chunk_size)
            # 讀到檔尾會回傳空字串，空字串被視為False，所以"not chunk"成立就代表資料已經讀完
            if not chunk:
                break
            # 將暫存資料寫入目的檔案
            fd.write(chunk)


def main():
    readDir = "read"
    # 存放目錄不存在就建立，相對路徑代表存放位置跟執行的Python檔案放在同一目錄
    writeDir = "write"
    if not os.path.isdir(writeDir):
        os.makedirs(writeDir)
    
    print("---demoReadWriteBinary()------------")
    demoReadWriteBinary(f"{readDir}/images.jpg", f"{writeDir}/binary.png")
    print("---demoReadWriteLarge()------------")
    demoReadWriteLarge(f"{readDir}/image1.jpg", f"{writeDir}/binaryLarge.png")


main()