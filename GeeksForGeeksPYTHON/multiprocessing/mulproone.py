import time
import multiprocessing

def cal_sq(numbers):
    print("Calculating squares:")
    for i in numbers:
        time.sleep(5)
        print("Square",i*i)

def cal_cube(numbers):
    print("Calculating cubes:")
    for i in numbers:
        time.sleep(5)
        print("Cube",i*i*i)

if __name__=="__main__":
    numbers=[3,4,5,6]

    processone=multiprocessing.Process(target=cal_sq,args=(numbers,))
    processtwo=multiprocessing.Process(target=cal_cube,args=(numbers,))

    processone.start()
    processtwo.start()

    processone.join()
    processtwo.join()

    print("Done")

