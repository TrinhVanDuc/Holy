def print_map(function, iterable):
    iter_obj = iter(iterable)
    while True:
        try:
        # get the next item
            element = next(iter_obj)
            print(function(element))
        except StopIteration:
        # if StopIteration is raised, break from loop
            break
