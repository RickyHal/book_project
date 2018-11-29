# break_for.py
inputStr = input("请输入字符串：")
print("输入的字符串为：" + inputStr)
for item in inputStr:
    if item == "_":
        print("输入的字符串包含下划线")
        break
    else:
        print(item)
