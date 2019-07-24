# break_for.py
#!/usr/bin/env python3
inpu_str = input("请输入字符串：")
print("输入的字符串为：" + inpu_str)
for item in inpu_str:
    if item == "_":
        print("输入的字符串包含下划线")
        break
    else:
        print(item)
