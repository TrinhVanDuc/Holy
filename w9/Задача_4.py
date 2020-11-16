class Terminate(Exception):
    pass

class Connect(Exception):
    pass

def connect_user(users):
    with open('users.txt','w') as f:
        yield from write_to_file(f)

def write_to_file(f_obj):
    while True:
        try:
            x = yield
            print(f"Inner: {x}")
            f_obj.writelines(x)
        except Terminate:
            print('Finished')
            break
    f_obj.close()

def Task_Manager():
    print("Task Manager started")
    u = []
    while True:
        try:
            x = yield
            print(f"Outer: {x}")
            u.append(x)
        except Connect:
            yield from connect_user(u)

try:
    coroutine = Task_Manager()
    next(coroutine)
    coroutine.send('luffy')
    coroutine.send('Zoro')
    coroutine.throw(Connect)
    coroutine.send('exercise')
    coroutine.send('news')
    coroutine.throw(Terminate)
except:
    pass






