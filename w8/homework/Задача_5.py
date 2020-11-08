import itertools
def get_permutations(s, n):
    try:
        return sorted(list(''.join(i) for i in itertools.permutations(s,n)))
    except Exception:
        raise RuntimeError("Not implemented")
