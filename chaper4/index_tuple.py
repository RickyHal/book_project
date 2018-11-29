# index_tuple.py
tuple_C = ("Python", "Java", "C")
print(tuple_C[0] + " " + tuple_C[1] + " " + tuple_C[2])
for item in tuple_C:  # 使用for循环遍历元组
    print(item, end=" ")
print()
i = 0
while i < len(tuple_C):  # 使用while循环遍历元组
    print(tuple_C[i], end=" ")
    i += 1
