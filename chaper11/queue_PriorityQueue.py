# queue_PriorityQueue.py
import queue

# 创建PriorityQueue队列
q = queue.PriorityQueue(3)
# 打印队列是否为空
print('队列是否为空：', q.empty())
# 打印队列size
print('写入前队列size：', q.qsize())
print('写入一个元素：', (10, 'a'))
q.put((10, 'a'))
print('写入一个元素：', (-1, 'b'))
q.put((-1, 'b'))
print('写入一个元素：', (100, 'c'))
q.put((100, 'c'))
print('写入后队列size：', q.qsize())
# 打印队列是否已满
print('队列是否已满：', q.full())
while not q.empty():
    print('读取一个元素：', q.get())
print('读取后队列size：', q.qsize())
