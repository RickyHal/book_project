# tuple_for_while.py
#!/usr/bin/env python3
tuple_1 = ("Python", "Java", "C")
print(tuple_1[0] + " " + tuple_1[1] + " " + tuple_1[2])
for item in tuple_1:  # 使用for循环遍历元组
    print(item, end=" ")
print()
i = 0
while i < len(tuple_1):  # 使用while循环遍历元组
    print(tuple_1[i], end=" ")
    i += 1
