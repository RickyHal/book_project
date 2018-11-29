# queue_LIFO.py
import queue

# 创建LIFO队列
q = queue.LifoQueue(3)
# 打印队列是否为空
print('队列是否为空：', q.empty())
# 打印队列size
print('写入前队列size：', q.qsize())
for i in range(3):
    # 写入i到队列q
    print('写入一个元素', i)
    q.put(i)
print('写入后队列size：', q.qsize())
# 打印队列是否已满
print('队列是否已满：', q.full())
while not q.empty():
    print('读取一个元素：', q.get())
print('读取后队列size：', q.qsize())
