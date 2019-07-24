import time
import os
import random
from multiprocessing import Pool, Manager, Queue


def createFile(file_name):
    with open(file_name, 'w') as f:
        while os.path.getsize(file_name) < 1024 * 1024:
            string = str(random.randint(0, 100000)) + '\n'
            print(string)
            f.write(string)
if __name__ == "__main__":
    length = 10
    p = Pool(length)
    for i in range(length):
        file_name = 'file' + str((i + 1)) + '.txt'
        p.apply_async(createFile, args=(file_name,))
    p.close()
    p.join()
