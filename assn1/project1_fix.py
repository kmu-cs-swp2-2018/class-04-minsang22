import time

def iterfibo(nbr):
#변수 이름을 처음엔 a, b로 코드를 짰었는데 조원들과 리뷰를 하며 변수 이름이
#a, b라면 너무 피보나치 수열을 짰다는 목적이 담기지 않는 것 같다는 의견을 받아
#변수명을 피보나치 수열의 n, m번째 항이라는 의미로 fn, fm으로 수정하였다.
    fn, fm = 0, 1
    if nbr == 0:
        return 0
    if nbr == 1:
        return 1
    if nbr > 1:
        for i in range( 0, nbr ):
            fn, fm = fm, fn + fm
        return fn


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