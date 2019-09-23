import time

def iterfibo(nbr):
    fn, fm = 0, 1
    # 피보나치 수열을 for문을 돌리면서 계산시켜줄 변수를 각각 수열의 n, m번째 항이라는 의미를 담아 fn, fm으로 설정했다.
    if nbr == 0: 
        return 0
    # 피보나치 수열의 0번째 항은 0이라는 값이 고정이기 때문에 변수 nbr에 0이 들어갈 때 0을 리턴하도록 했다.
    if nbr == 1:
        return 1
    # 위와 같이, 피보나치 수열의 1번째 항 또한 1로 고정이기 때문에 변수 nbr에 1이 들어갈 때 1을 리턴하도록 했다.
    if nbr > 1:
    # nbr에 2 이상의 수가 들어갈 경우 피보나치 수열의 nbr번째 항을 계산해 줄 코드를 설정해주었다.
        for i in range( 0, nbr ):
    # for 반복문을 통해 총 nbr번 만큼의 계산을 해 nbr번째 항을 구하도록 했다.
            fn, fm = fm, fn + fm
    # for문의 반복이 한 번 돌아갈 때마다 fn 자리에는 다음 항인 fm을, fm 자리에는 fn + fm을 한 fm 다음 번째의 항의 값을 저장하도록 했다.
        return fn
    # 결국 최종적으로 nbr번만큼 계산을 해줬으므로 fn 자리에 저장되어 있는 값이 nbr번째의 피보나치 수열의 값이고 이를 리턴해준다. 


def fibo(n):
    if n <= 1:
        return n
    return fibo( n - 1 ) + fibo( n - 2 )
    # 피보나치 수열의 정의 그대로를 재귀함수를 이용해 바로 짠 코드이다. 코드를 짜기엔 굉장히 쉽지만 재귀함수가 계속 호출되는 시간이 필요하므로
    # n의 크기가 커질수록 피보나치 수열의 값을 계산하는 시간이 굉장히 길어진다.





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
    # 처음 시간을 저장해 주고 계산이 끝난 후의 시간에서 처음 저장한 시간을 빼 수열을 계산하는데 걸린 시간을 계산해주는 코드이다.
    # 먼저 for 반복문을 사용해 피보나치 수열을 계산하는 데 걸린 시간을 출력해 주고 그 다음줄에는 재귀함수를 사용했을 때 걸린 시간을 출력해준다.
