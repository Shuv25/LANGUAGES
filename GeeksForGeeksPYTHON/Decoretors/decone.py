import time

def time_it(func):
    def wrapper(*args,**keywords):
        start=time.time()
        res=func(*args,**keywords)
        end=time.time()
        print(func.__name__+" took "+str((end-start)*1000)+" mili second")
        return res
    return wrapper

@time_it
def cal_sq(numbers):
    res=[]
    for i in numbers:
        res.append(i*i)
    return res

@time_it
def cal_cube(numbers):
    res=[]
    for i in numbers:
        res.append(i*i*i)
    return res

array=range(1,100000)
sq=cal_sq(array)
cu=cal_cube(array)
