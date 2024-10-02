names = ["Python", "Java", "JS", "Swift", "C#"]
print(f"names: {names}")
name = "MySQL"

# 檢查 name 是否存在於 names
if name in names:
    names.remove(name)
    print("after removing \"MySQL\": ")
else:
    names.append(name)
    print("after appending \"MySQL\": ")

print(f"names: {names}")
