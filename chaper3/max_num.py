# max_num.py
#!/usr/bin/env python3
num_a = float(input("请输入数字A："))
num_b = float(input("请输入数字B："))
max_num = num_a if num_a > num_b else num_b
print("max_num is:" + str(max_num))
