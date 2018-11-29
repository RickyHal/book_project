# fromkeys_1.py
keys = ['Apple', 'Orange', 'Breed']
dict_A = dict.fromkeys(keys)  # 没有values参数
dict_B = dict.fromkeys(keys, 8)  # 有values参数
print(dict_A)
print(dict_B)
