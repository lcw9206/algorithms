# Recursive Algorithms

## 재귀 함수 (recursive functions)란?
> * 하나의 함수에서 자신을 다시 호출하여 작업을 수행하는 것으로 생각보다 많은 문제를 재귀적으로 해결할 수 있다.
> * 재귀 함수에서 종결조건은 필수로 지정해야한다.

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

