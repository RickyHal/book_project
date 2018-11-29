# login5.py
userName = input("请输入用户名：")
passwd = input("请输入密码：")
if userName == "admin" and passwd == "123":
    print("你好" + userName)
    print("登录成功")
elif userName == "admin" and passwd != "123":
    print("密码错误")
elif userName.find("_") != -1:  # 查找到了输入的用户名中有下划线
    print("用户名格式不正确")
else:
    print("用户" + userName + "不存在")
