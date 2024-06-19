import multiprocessing
import time

def deposit(amount,lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        amount.value=amount.value+1
        lock.release()

def witdaw(amount,lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        amount.value=amount.value-1
        lock.release()

if __name__=="__main__":
    amount=multiprocessing.Value('i',300)
    lock=multiprocessing.Lock()
    proone=multiprocessing.Process(target=deposit,args=(amount,lock))
    protwo=multiprocessing.Process(target=witdaw,args=(amount,lock))

    proone.start()
    protwo.start()
    proone.join()
    protwo.join()

    print(amount.value)