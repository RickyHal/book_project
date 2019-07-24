# dict_for_2.py
#!/usr/bin/env python3
dict_2 = {'name': 'Jack', 'age': 20, 'sex': 'Male'}
print("key-value:")
for key, value in dict_2.items():  # 同时遍历键和值
    print(key + ":" + str(value), end=",")
print("\nkeys:")
for key in dict_2.keys():  # 遍历键
    print(key, end=" ")
print("\nvalues:")
for value in dict_2.values():  # 遍历
    print(value, end=" ")
