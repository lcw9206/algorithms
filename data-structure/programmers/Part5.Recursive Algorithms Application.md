# Recursive Algorithms Application

## 조합의 수
n 개의 서로 다른 원소에서 m개를 선택하는 경우의 수를 일반적인 방법과 재귀적인 방법으로 구해보자.
```
############ 일반적인 방법
from math import factorial as p

def combi(n,m):
    return f(n) / (f(m) * f(n-m))
    
############ 재귀적인 방법
def combi(n,m):
    if n == m:
        return 1
    elif m == 0:
        return 1
    else:
        return combi(n-1, m) + combi(n-1, m-1)
```
재귀적인 방법은 지속적으로 함수를 재호출하므로 효율적이지 않다는 것을 알 수 있다.

## 재귀함수의 실행시간 비교해보기
그렇다면 재귀함수와 일반 반복문의 효율성을 따져보도록 하자.
```
import time

############ 재귀함수
def rec(n):
    if n <= 1:
        return n
    else:
        return rec(n - 1) + rec(n - 2)

############ 반복함수
def iter(n):
    if n <= 1:
        return n
    else:
        i = 2
        t0 = 0
        t1 = 1
        while i <= n:
            t0, t1 = t1, t0 + t1
            i += 1
        return t1
       
############ 시간측정 구문
while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break
    
    ts = time.time()
    fibo = iter(nbr)
    ts = time.time() - ts
    print("Iterative version: %d (%.3f)" % (fibo, ts))
    ts = time.time()
    fibo = rec(nbr)
    ts = time.time() - ts
    print("Recursive version: %d (%.3f)" % (fibo, ts))

############ 시간측정 결과 
Enter a number: 20
Iterative version: 6765 (0.000)
Recursive version: 6765 (0.004)
Enter a number: 30
Iterative version: 832040 (0.000)
Recursive version: 832040 (0.471)
```
20번째의 순열까지는 비슷한 시간이 걸리나, 30번째 이상의 순열부터 속도 차이가 나는 것을 볼 수 있다.

## 실습1. 재귀적 이진 탐색 구현
```
def solution(L, x, l, u):
    if l > u:
        return -1
    mid = (l + u) // 2
    
    if x == L[mid]:
        return mid
    elif x < L[mid]:
        return solution(L, x, l, mid - 1)
    else:
        return solution(L, x, u, mid + 1)
```

## 실습2. 하노이의 탑 (재귀)
* n개의 원반을 최종적으로 도착기둥으로 옮기는 것이 목표로 대표적인 재귀함수의 예다.
> 1. n-1개의 원반을 중간기둥으로 옮긴다.
> 2. n번째의 원반을 도착기둥으로 옮긴다.
> 3. n-1개의 원반을 중간기둥에서 도착기둥으로 옮긴다.
```
def hanoi(n, startp, wayp, endp):
    if n == 1:
        print('{}번 원반을 {}에서 {}로 옮겼습니다.'.format(n, startp, endp))
        return
    else:
        hanoi(n-1, startp, endp, wayp)
        print('{}번 원반을 {}에서 {}로 옮겼습니다.'.format(n, startp, endp))
        hanoi(n-1, wayp, startp, endp)
```
