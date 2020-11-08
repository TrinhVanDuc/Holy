import itertools

def maximize(lists, m):
    try:
        list_max2_element = list(max(i)**2 for i in lists)
        list_sum = list(i for i in itertools.accumulate(list_max2_element))
        return max(list_sum) % m
    except Exception:
        raise RuntimeError("Not implemented")
