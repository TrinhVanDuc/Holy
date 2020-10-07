def primes():
    x = 2
    while 1:
        x += 1
        for i in range(2, x):
            if x % i == 0:
                break
            elif i == x - 1:
                yield x
add_primes = primes()
import argparse
import sys
parser = argparse.ArgumentParser()
parser.add_argument('-a','--show-a',action='store_true',default=False)
parser.add_argument('-f','--file',type=argparse.FileType('w',encoding='utf8'))
parser.add_argument('num', type=int)
args = parser.parse_args()

pr = args.num
collection = []
for i in range(pr):
    si = next(add_primes)
    collection.append(si)
write ='{}th number prime:{}'.format(pr,si)
print(write)
if args.file:
    print(write, file= args.file)
if args.show_a==True:
    print(*collection)
    if args.file:
        print(*collection, file= args.file)
if args.file is not None:
    args.file.close()
                     
