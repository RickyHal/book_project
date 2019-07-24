# yield_line.py
#!/usr/bin/env python3


# 生成器方式读取
def read_data():
    with open('file_2.txt', 'r') as f:
        for line in f:
            # 以生成器的方式返回一行内容
            yield line


# 列表形式读取
def read_data_list():
    data = []
    with open('file_2.txt', 'r') as f:
        for line in f:
            data.append(line)
    return data


for line in read_data():
    print(line)
