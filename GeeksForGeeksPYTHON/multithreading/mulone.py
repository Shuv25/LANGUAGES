import time
import threading

def cal_sq(numbers):
    print("Calculating squares:")
    for i in numbers:
        time.sleep(0.2)
        print("Square",i*i)

def cal_cube(numbers):
    print("Calculating cubes:")
    for i in numbers:
        time.sleep(0.2)
        print("Cube",i*i*i)

numbers=[3,4,5,6]

t=time.time()

threadone=threading.Thread(target=cal_sq,args=(numbers,))
threadtwo=threading.Thread(target=cal_cube,args=(numbers,))

threadone.start()
threadtwo.start()

threadone.join()
threadtwo.join()

print("Time taken"+str(time.time()-t))


