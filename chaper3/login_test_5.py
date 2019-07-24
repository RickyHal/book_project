# login_test_5.py
#!/usr/bin/env python3
user_name = input("请输入用户名：")
passwd = input("请输入密码：")
if user_name == "admin" and passwd == "123":
    print("你好" + user_name)
    print("登录成功")
elif user_name == "admin" and passwd != "123":
    print("密码错误")
elif user_name.find("_") != -1:  # 查找到了输入的用户名中有下划线
    print("用户名格式不正确")
else:
    print("用户" + user_name + "不存在")
