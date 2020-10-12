import time
from functools import wraps
def rabofile(file):
    def timmer(func):
        @wraps(func)
        def wrapper_timer(*args,**kwargs):
            start_time = time.perf_counter()
            otviet = func(*args,**kwargs)
            end_time = time.perf_counter()
            run_time = end_time - start_time
            with open(file,'w') as f:
                f.write('Start time:{}'.format(start_time))
                f.write('Arg:{}'.format(args))
                f.write('Otviet: {}'.format(otviet) if otviet else '-')
                f.write('End time:{}'.format(end_time))
                f.write('Run_time:{}'.format(run_time))
            return otviet
        return wrapper_timer
    return timmer
@rabofile('new.txt')
def div(x,y):
    res = x+y
    print(res)
div(2,3)






