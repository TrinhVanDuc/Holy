import itertools

def compress_string(s):
    a = itertools.groupby(s)
    b = []
    c = []
    for key, group in a:
        b.append(int(key))
        c.append(len(list(group)))
    return list(zip(c,b))

