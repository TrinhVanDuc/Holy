import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--n', dest='p1')
args = parser.parse_args()
n = int(args.p1)
def f(i):
    if i in (1, 2):
        return 1
    return f(i - 1) + f(i - 2)
print(f(n))
