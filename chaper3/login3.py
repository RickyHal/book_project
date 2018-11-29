# login3.py
userName = input("请输入用户名：")
if userName == "admin":
    print("你好" + userName)
elif userName.find("_") != -1:  # 查找到了输入的用户名中有下划线
    print("用户名格式不正确")
else:
    print("用户" + userName + "不存在")
