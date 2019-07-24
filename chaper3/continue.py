# continue.py
#!/usr/bin/env python3
for i in range(1, 11):
    if i % 2 == 0:  # 当前遍历的数除2余数为0
        continue
    print(i)
