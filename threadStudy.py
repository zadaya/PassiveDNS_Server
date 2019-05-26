import time, threading

# 假定这是你的银行存款:
balance = 0

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        change_it(n)
def myThread():
    time.sleep(2)
    t1 = threading.Thread(target=run_thread, args=(66,))
    t2 = threading.Thread(target=run_thread, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print (balance)
t = threading.Thread(target=myThread)
t.start()
# join()调用后其他线程等待该线程结束后才被执行
t.join()
n = 0
while n < 5:
    n = n + 1
    print ('thread %s >>> %s' % (threading.current_thread().name, n))
    time.sleep(1)