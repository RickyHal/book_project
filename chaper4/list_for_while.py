# list_for_while.py
list_D = ["Py", "on", "th", 3, 7, "."]
for item in list_D:  # 使用for循环遍历列表
    print(item, end="")
print()  # 换行
i = 0
length = len(list_D)
while i < length:  # 使用while循环遍历列表
    print(list_D[i], end="")
    i += 1
