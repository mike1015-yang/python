import os
from datetime import datetime


def main():
    print("---顯示使用者家目錄資訊-------------")
    # 取得使用者家目錄
    # "~"或"~user"代表指定使用者家目錄
    userHome = os.path.expanduser("~")
    print(f"user's home directory: {userHome}")
    # dirname: 取得檔案的父目錄
    print(f"parent directory path: {os.path.dirname(userHome)}")
    # isfile: 檢查是不是檔案
    print(f"isfile: {os.path.isfile(userHome)}")
    # isdir: 檢查是不是目錄
    print(f"isdir: {os.path.isdir(userHome)}")
    # 取得建立時間
    print(f"create time: {datetime.fromtimestamp(os.path.getctime(userHome))}")
    # 取得家目錄裡的內容(字串)
    print("listdir(): " + ", ".join(os.listdir(userHome)))

    print("---建立目錄-----------------------")
    dir1 = f"{userHome}/testDir/dir1"
    if os.path.exists(dir1):
        print(f"{dir1} exists")
    else:
        # 路徑中所有不存在的目錄都會建立
        os.makedirs(dir1)
        print(f"{dir1} is created")

    print("---建立檔案-----------------------")
    file1 = f"{userHome}/testDir/dir1/file1.txt"
    # 檔案不存在時會建立，檔案已存在時會覆蓋
    # 'w'('wt'): 寫文字檔，用UTF-8的編碼來寫
    with open(file1, "w", encoding="UTF-8") as f:
        f.write("Hello")
    print(f"{file1} is created")

    print("---檔案搬移兼更名------------------")
    file2 = f"{userHome}/testDir/file2.txt"
    os.rename(file1, file2)
    print(f"{file1} is renamed to {file2}")

    print("---刪除檔案-----------------------")
    if os.path.exists(file2) and os.path.isfile(file2):
        os.remove(file2)
        print(f"{file2} is removed")

    print("---刪除目錄-----------------------")
    if os.path.exists(dir1) and os.path.isdir(dir1):
        os.rmdir(dir1)
        print(f"{dir1} is removed")

main()