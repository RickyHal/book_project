# tuple_return.py
def tuple_return():  # 定义一个函数
    a = 'Hello'
    b = 'Python'
    return a, b  # 返回一个包含变量a和变量b的元组
nums = tuple_return()  # 接收返回值
print(nums[0] + " " + nums[1])  # 打印返回的多个值
