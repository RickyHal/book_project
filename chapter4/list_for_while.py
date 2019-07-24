# list_for_while.py
#!/usr/bin/env python3
list_1 = ["Py", "on", "th", 3, 7, "."]
for item in list_1:  # 使用for循环遍历列表
    print(item, end="")
print('\n')  # 换行
i = 0
while i < len(list_1):  # 使用while循环遍历列表
    print(list_1[i], end="")
    i += 1
