# remove_num.py
num = '0123456789'
string = "vsfe86sf4g5rv14a5"
new_list = [item for item in list(string) if item not in num]
new_string = "".join(new_list)  # 列表转字符串
print(new_string)
