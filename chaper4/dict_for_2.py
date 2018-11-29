# dict_for_2.py
dict_A = {'name': 'Jack', 'age': 20, 'sex': 'Male'}
print("key-value:")
for key, value in dict_A.items():  # 同时遍历键和值
    print(key + ":" + str(value), end=",")
print("\nkeys:")
for key in dict_A.keys():  # 遍历键
    print(key, end=" ")
print("\nvalues:")
for value in dict_A.values():  # 遍历
    print(value, end=" ")
