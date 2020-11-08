import itertools

def compress_string(s):
    try:
        a = itertools.groupby(s)
        b = []
        c = []
        for key, group in a:
            b.append(int(key))
            c.append(len(list(group)))
        return list(zip(c,b))
    except Exception:
        raise RuntimeError("Not implemented")
