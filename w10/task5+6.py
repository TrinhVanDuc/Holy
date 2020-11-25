import threading
import matplotlib.pyplot as plt
import time

# task 5
a = 0
def scalar_product(x1, x2):
    global a
    s = x1*x2
    a = a + s

def run_threads(n,v1,v2):
    threads = [threading.Thread(target= scalar_product, args = (v1[i],v2[i])) for i in range(n)]
    for thread in threads:
        thread.start()

v1 = [150519992020,301220002020,181019992020,221119942020,112119992020]
v2 = [300120002020,230519992020,301119992020,100819762020,201119992020]
n = len(v1)
start_time = time.time()
run_threads(n,v1,v2)
run_time = time.time() - start_time
print ('Finished.\nScalar product is: {}.\nRuntime is: {}.'.format(a,run_time))

# task 6
def scalar(v1,v2):
    a = 0
    for i in range(len(v1)):
        a += v1[i]*v2[i]
        return a

x_data = [1, 2, 3, 8, 10, 12] # Number of threads
list_time = []
for i in range(3):
    start_time1 = time.time()
    scalar(v1,v2)
    run_time1 = time.time() - start_time1
    list_time.append(run_time1)
for i in range(3):
    start_time2 = time.time()
    run_threads(n,v1,v2)
    run_time2 = time.time() - start_time2
    list_time.append(run_time2)

print(list_time)
plt.plot(x_data, list_time)
plt.grid()
plt.ylabel('Время выполнения, [с]')
plt.xlabel('Число потоков')
plt.show()
