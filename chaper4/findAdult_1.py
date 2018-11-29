# findAdult_1.py
age = [12, 6, 30, 52, 3, 42, 8, 18]
adult = []
for item in age:
    if item >= 18:  # 判断年龄是否>=18
        adult.append(item)
adult.sort()
print(adult)
