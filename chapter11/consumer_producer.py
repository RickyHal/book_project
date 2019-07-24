# consumer_producer.py
import threading
import time
from queue import Queue


# 消费者
class Consumer(threading.Thread):

    def __init__(self, lock, product):
        super(Consumer, self).__init__()
        self.lock = lock
        self.product = product

    def run(self):  # 定义run方法
        while True:
            # 申请锁
            self.lock.acquire()
            if self.product.qsize() > 0:
                # 消耗一件商品
                self.product.get()
                print("消费者：消费1件商品,剩余库存", self.product.qsize())
                self.lock.notify()
                # 释放锁
                self.lock.release()
                time.sleep(2)
            else:
                print("商品库存不够，等待生产者生产商品")
                self.lock.wait()

# 生产者


class Producer(threading.Thread):

    def __init__(self, lock, product):
        super(Producer, self).__init__()
        self.lock = lock
        self.product = product

    def run(self):  # 定义run方法
        while True:
            # 申请锁
            self.lock.acquire()
            if self.product.qsize() < 3:
                self.product.put('product')
                print("生产者：生产1件商品,剩余库存", self.product.qsize())
                self.lock.notify()
                # 释放锁
                self.lock.release()
                time.sleep(1)
            else:
                print("商品库存已满，等待消费者消费商品")
                self.lock.wait()

if __name__ == "__main__":
    lock = threading.Condition()
    # 创建商品队列
    product = Queue(maxsize=3)
    print('初始库存：', product.qsize())
    # 创建消费者线程
    consumer = Consumer(lock, product)
    # 创建生产者线程
    producer = Producer(lock, product)
    producer.start()
    consumer.start()
    producer.join()
    consumer.join()
