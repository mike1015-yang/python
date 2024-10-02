import os
from PIL import Image


def demoReadImage(file):
    with Image.open(file) as image:
        print(f"image.format: {image.format}")
        print(f"image.size: {image.size}")
        print(f"image.mode: {image.mode}")


def demoReadWriteImage(source, destination):
    with Image.open(source) as image:
        image.save(destination)


def main():
    readDir = "read"
    # 存放目錄不存在就建立，相對路徑代表存放位置跟執行的Python檔案放在同一目錄
    writeDir = "write"
    if not os.path.isdir(writeDir):
        os.makedirs(writeDir)

    print("---demoReadImage()------------")
    demoReadImage(f"{readDir}/image2.png")
    print("---demoReadWriteImage()------------")
    demoReadWriteImage(f"{readDir}/image2.png", f"{writeDir}/image.png")


main()
