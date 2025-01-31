import time

def iterfibo(nbr):
    a,b = 0, 1
    if nbr == 0:
        return 0
    if nbr == 1:
        return 1
    if nbr>1:
        for i in range(0,nbr):
            a, b = b, a+b
        return a


def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)





while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1 :
        break
    ts = time.time()
    fibonumber = iterfibo(nbr)
    ts = time.time() - ts
    print("IterFibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() - ts
    print("Fibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))