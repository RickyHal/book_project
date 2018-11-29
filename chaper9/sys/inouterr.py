# inouterr.py
import sys

sys.stdout.write('请输入被除数：\n')
a = int(sys.stdin.readline())
sys.stdout.write('请输入除数：\n')
b = int(sys.stdin.readline())
if b == 0:
    sys.stderr.write('被除数不能为0')
else:
    sys.stdout.write(str(a / b) + '\n')
