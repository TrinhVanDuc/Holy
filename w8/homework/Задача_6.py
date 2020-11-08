import itertools

def get_combinations(s, n):
    try:
        list_combinations = sorted(list(''.join(sorted(x)) for i in range(1,n+1) for x in itertools.combinations(s,i)))
        list_combinations.sort(key= lambda x: len(x))
        return list_combinations
    except Exception:
        raise RuntimeError("Not implemented")
                                            
