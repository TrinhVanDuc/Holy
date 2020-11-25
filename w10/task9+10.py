import multiprocessing
from multiprocessing import Queue, Pipe
import matplotlib.pyplot as plt
import time
def product(x,y):
    return x * y

def f(q, res): # с помощью Queue
    q.put(res)
    return q

def f1(q, res): # с помощью Pipe
    q.send(res)
    q.close()
    pass

a = 0
def add_sum(q,counter):
    global a
    for i in range(counter):
        #res = q.get()         # с помощью Queue
        res = q.recv()         # с помощью Pipe

        a += res
    return a

def run_processes(counter,v1,v2,q):
    #processes = [multiprocessing.Process(target=f, args = (q,product(v1[i],v2[i]))) for i in range(0,counter)]  #Queue
    processes = [multiprocessing.Process(target=f1, args=(v, product(v1[i], v2[i]))) for i in range(0, counter)] #Pipe

    for process in processes:
        process.start()
    for process in processes:
        process.join()
    add_sum(q,counter)

def scalar(v1,v2):
    a = 0
    for i in range(len(v1)):
        a += v1[i]*v2[i]
        return a

if __name__ == "__main__":
    #q = Queue()
    q, v = Pipe()
    v1 = [23, 5, 1999, 15, 99]
    v2 = [31, 1, 2000, 30, 12]
    n = len(v1)
    start_time = time.time()
    run_processes(n, v1, v2, q)
    run_time = time.time() - start_time
    print('Finished\nScalar product is: {}. Runtime is: {}.'.format(a, run_time))
    x_data = [1, 2, 3, 8, 10, 12]  # Number of process
    list_time = []
    for i in range(3):
        start_time1 = time.time()
        scalar(v1, v2)
        run_time1 = time.time() - start_time1
        list_time.append(run_time1)
    for i in range(3):
        start_time2 = time.time()
        run_processes(n, v1, v2,q)
        run_time2 = time.time() - start_time2
        list_time.append(run_time2)

    print(list_time)
    plt.plot(x_data, list_time)
    plt.grid()
    plt.ylabel('Время выполнения, [с]')
    plt.xlabel('Число процессы')
    plt.show()
    
