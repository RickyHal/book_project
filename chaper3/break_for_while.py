# break_for_while.py
inputStr = input("请输入字符串：")
while inputStr != "-1":  # 循环1
    print("输入的字符串为：" + inputStr)
    for item in inputStr:  # 循环2
        if item == "_":
            print("输入的字符串包含下划线")
            break
        else:
            print(item)
    inputStr = input("请输入字符串：")
