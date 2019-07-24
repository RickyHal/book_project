# login_test_4.py
#!/usr/bin/env python3
user_name = input("请输入用户名：")
if user_name == "admin":
    print("你好" + user_name)
    passwd = input("请输入密码：")
    # 因为input（）函数的返回值始终是字符串，所以passwd应为字符串"123"，而不是数字123
    if passwd == "123":
        print("登录成功")
    else:
        print("密码错误")
elif user_name.find("_") != -1:  # 查找到了输入的用户名中有下划线
    print("用户名格式不正确")
else:
    print("用户" + user_name + "不存在")
