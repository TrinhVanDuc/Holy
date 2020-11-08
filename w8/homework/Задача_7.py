import itertools

def get_combinations_with_r(s, n):
    try:
        return sorted(list(''.join(sorted(i)) for i in itertools.combinations_with_replacement(s,n)))
    except:
        raise RuntimeError("Not implemented")
