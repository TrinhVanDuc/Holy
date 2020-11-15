def analis_zip(*iterable):
    sentinal = object
    iterators = [iter(it) for it in iterable]
    num_active = len(iterators)
    if not num_active:
        return
    while True:
        values = []
        for  it in (iterators):
            value = next(it,sentinal)
            if value is sentinal:
                return
            values.append(value)
        yield tuple(values)

def analis_map(function, iterable):
    for i in iterable:
        yield function(i)

def analis_enumerate(iterable, start=0):
    n = start
    for i in iterable:
        yield n,i
        n +=1
