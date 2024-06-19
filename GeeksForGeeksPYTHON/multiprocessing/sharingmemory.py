import multiprocessing

def cal_sq(numbers,result):
    print("Calculating squares:")
    for i,n in enumerate(numbers):
        result[i]=n*n

if __name__=="__main__":
    numbers=[3,4,5,6]
    result=multiprocessing.Array('i',4)
    processone=multiprocessing.Process(target=cal_sq,args=(numbers,result))

    processone.start()
    processone.join()

    print(result[:])

