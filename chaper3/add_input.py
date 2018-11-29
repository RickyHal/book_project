# add_input.py
num = int(input("请输入整数："))
sum = 0
while num != -1:
    sum = sum + num
    num = int(input("请输入整数："))
print("输入的所有整数之和为%d" % (sum))
