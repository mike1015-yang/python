from pathlib import Path
from datetime import datetime


def main():
    print("---顯示使用者家目錄資訊-------------")
    ## 取得使用者家目錄
    # "~"或"~user"代表使用者家目錄，但Windows系統可能不支援
    # userHome = os.path.expanduser("~")
    # 建議改用Python 3.5開始支援的pathlib.Path以確保支援Windows系統
    userHome = Path.home()
    print(f"user's home directory: {userHome}")
    print(f"parent directory path: {userHome.parent}")
    print(f"isfile: {userHome.is_file()}")
    print(f"isdir: {userHome.is_dir()}")
    print(f"create time: {datetime.fromtimestamp(userHome.stat().st_ctime)}")
    # 取得家目錄裡的內容(物件)
    print("for each item: " + ", ".join([item.name for item in userHome.iterdir()]))

    print("---建立目錄-----------------------")
    dir1 = Path(f"{userHome}/testDir/dir1")
    if dir1.exists():
        print(f"{dir1} exists")
    else:
        # "parents=True"則路徑中所有不存在的目錄都會建立
        dir1.mkdir(parents=True)
        print(f"{dir1} is created")
    
    print("---建立檔案-----------------------")
    file1 = Path(f"{userHome}/testDir/dir1/file1.txt")
    # 檔案不存在時會建立
    if file1.exists():
        print(f"{file1} exists")
    else:
        file1.touch()
        file1.write_text('hell0')
        print(f"{file1} is created")
    
    print("---檔案搬移兼更名------------------")
    file2 = Path(f"{userHome}/testDir/file2.txt")
    file1.rename(file2)
    print(f"{file1} is renamed to {file2}")
    
    # print("---刪除檔案-----------------------")
    # if file2.exists():
    #     file2.unlink()
    #     print(f"{file2} is removed")

    # print("---刪除目錄-----------------------")
    # if dir1.exists() and dir1.is_dir():
    #     dir1.rmdir()
    #     print(f"{dir1} is removed")


main()
