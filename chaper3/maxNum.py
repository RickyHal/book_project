# maxNum.py
numA = float(input("请输入数字A："))
numB = float(input("请输入数字B："))
maxNum = numA if numA > numB else numB
print("maxNum is:" + str(maxNum))
