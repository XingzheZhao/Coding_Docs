import threading
import time


# def func():
#     print('ran')
#     time.sleep(1)
#     print('almost done')
#     time.sleep(0.85)
#     print('done')


# # ! creating an thread object
# x = threading.Thread(target=func)
# x.start()
# print(threading.activeCount())
# time.sleep(1.2)
# print('finally')


ls = []

def count_1(n):
    for i in range(1, n+1):
        print(f'function count_1 {i}')
        ls.append(i)
        time.sleep(0.01)

def count_2(n):
    for i in range(1, n+1):
        print(f'function count_2 {i}')
        ls.append(i)
        time.sleep(0.05)

x = threading.Thread(target=count_1, args=(5,))
x.start()

y = threading.Thread(target=count_2, args=(5,))
y.start()

x.join()
y.join()

print(ls)