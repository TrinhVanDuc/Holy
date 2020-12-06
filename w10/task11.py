from multiprocessing import Pool

def scalar1(x,y): # by pool.apply
    return x * y

def scalar2(x): # by pool.map
    return x[0] * x[1]

if __name__ == "__main__":
    v1 = [1, 2, 3]
    v2 = [4, 5, 6]
    pool = Pool(processes=5)
    results1 = [pool.apply(scalar1, args=(i, j)) for i, j in zip(v1, v2)]
    print(sum(results1))
    results = pool.map(scalar2, zip(v1, v2))
    print(sum(results))
