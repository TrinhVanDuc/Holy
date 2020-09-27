class MyExeption (Exception):
    def __init__(self,arg):
        self.arg=arg

try:
    try:
        a = input()
        int(a)
    except:
        raise MyExeption("Convertion is failed")
except MyExeption as ex:
    print(ex.arg)
