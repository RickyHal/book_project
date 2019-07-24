# break_for_while.py
#!/usr/bin/env python3
inpu_str = input("请输入字符串：")
while inpu_str != "-1":  # 循环1
    print("输入的字符串为：" + inpu_str)
    for item in inpu_str:  # 循环2
        if item == "_":
            print("输入的字符串包含下划线")
            break
        else:
            print(item)
    inpu_str = input("请输入字符串：")
