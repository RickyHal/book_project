# login_test_3.py
#!/usr/bin/env python3
user_name = input("请输入用户名：")
if user_name == "admin":
    print("你好" + user_name)
elif user_name.find("_") != -1:  # 查找到了输入的用户名中有下划线
    print("用户名格式不正确")
else:
    print("用户" + user_name + "不存在")
