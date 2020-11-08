import itertools
def get_cartesian_product(a, b):
    try:
        return list(itertools.product(a,b))
    except Exception:
        raise RuntimeError("Not implemented")
