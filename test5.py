#Recoerd function"s nama and paramater when it is called

def logger(func):
    def inner(*args, **kvargs):
        print  func.__name__, 'called, arguments: ', args, kvargs
        func(*args, **kvargs)
    return inner

@logger
def myfunc(a, b):
    return a+b

@logger
def myfunc2(a, b, c):
    return a+b+c

myfunc(1, 2)
myfunc(3, 4)
myfunc2(1, 2, 3)
myfunc2(3, 4, 5)
                
