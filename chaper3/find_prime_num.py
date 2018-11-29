# find_prime_num.py
start = int(input("请输入起始位置："))
end = int(input("请输入结束位置："))
for i in range(start, end + 1):  # 循环1
    if start > 1:
        for j in range(2, i):  # 循环2
            if i % j == 0:  # 如果存在除了1和i自身外其它的因数
                break  # 跳出循环2
        else:
            print(i)  # 打印素数
