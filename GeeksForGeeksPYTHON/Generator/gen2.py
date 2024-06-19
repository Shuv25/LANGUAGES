def fib(n):
    f=0
    s=1
    i=1
    while(i<=n):
        t=f+s
        yield(f)
        f=s
        s=t
        i+=1

for j in fib(8):
    print(j)