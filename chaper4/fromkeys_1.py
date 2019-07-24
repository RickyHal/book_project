# fromkeys_1.py
#!/usr/bin/env python3
keys = ['Apple', 'Orange', 'Breed']
dict_1 = dict.fromkeys(keys)  # 没有values参数
dict_2 = dict.fromkeys(keys, 8)  # 有values参数
print(dict_1)
print(dict_2)
