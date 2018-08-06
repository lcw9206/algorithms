# Recursive Algorithms

## 재귀 함수(recursive functions)란?
> * 하나의 함수에서 자신을 다시 호출하여 작업을 수행하는 것으로 생각보다 많은 문제를 재귀적으로 해결할 수 있다.
> * 재귀 함수에서 종결 조건은 필수로 지정해야한다.

## 예제

### 1. 자연수의 합 구하기
> 1부터 n까지의 모든 자연수의 값을 구하시오.

```
def sum(n):
  if n <= 1:
    return n
  else:
    return n + sum(n-1)
```

### 2. factorial
> 1부터 n까지 모든 자연수의 곱을 구하시오.

```
def multi(n):
  if n <=1 :
    return 1
  else:
    return n * multi(n-1)
```

## 재귀 알고리즘의 효율
> * 모든 재귀 알고리즘(Recursive version)은 반복 알고리즘(Iterative version)이라는 반대되는 알고리즘을 갖는다.
> * 재귀 알고리즘의 효율성, 시간 복잡도가 항상 좋지는 않다는 것을 명심하자.

### 예시
```
재귀 알고리즘(Recursive version)        반복 알고리즘(Iterative version)
def sum(n):                          def sum(n):
  if n <= 1:                           s = 0
    return 1                           while s >= 0:
  else:                                  s += n
    return n + sum(n-1)                  n -= 1
                                       return s

* 위의 예는 재귀 알고리즘은 함수를 반복적으로 호출하는 작업이 필요하기 때문에 오히려 반복 알고리즘이 효율적이다.
```


### 실습1. 피보나치 순열 구현하기 (재귀)
```
def solution(x):
    if x <= 1:
        return x
    else:
        return solution(x-2) + solution(x-1)
```

### 실습2. 피보나치 순열 구현하기 (반복)
```
def solution(x):
    prev, curr = 0, 1
    for i in range(x):
        prev, curr = curr, prev + curr
    return prev
```

