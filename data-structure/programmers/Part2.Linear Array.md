# 선형배열 (Linear Arrays)


## 배열 (Arrays)
> * 같은 종류의 데이터를 순서대로 나열한 것으로, 다른 언어와 달리 파이썬에는 배열이 존재하지 않아 리스트를 사용한다.
> * 각 원소에는 인덱스가 붙어있으며, 0부터 시작한다.

## 리스트 (Lists)
> * 파이썬에서의 리스트는 타입 제한없이 데이터를 나열할 수 있는 범용적인 배열이라고 할 수 있다.

## O(1)의 실행시간을 갖는 연산들
> ### 1. append(val)
> * 리스트의 끝에 원소(val)를 추가한다. 
> ### 2. pop(n)
> * 리스트의 맨 끝(n이 없을 경우) 혹은 원하는 인덱스(n)의 요소를 return하며 삭제한다.

## 길이에 비례해 O(n)의 실행시간(선형시간)을 갖는 연산들
> ### 1. insert(n,val)
> * 원하는 위치(n)에 원소(val)를 삽입한다.
> ### 2. del(arr[n])
> * 리스트(arr)의 원하는 인덱스(n)의 원소를 삭제한다.
> ### 3. remove(n)
> * 리스트에서 원하는 요소(n)를 삭제한다.
> ### 4. index(n)
> * 리스트에서 원하는 원소(val)의 인덱스를 찾아 반환한다. 해당 원소가 없을 경우, ValueError를 발생시킨다.
 
## pop(n)과 del(n)의 차이점은?
>  * 두 연산 모두 특정 인덱스(n)의 원소를 지운다는 공통점이 있지만, pop은 원소를 return 후에 삭제하고, del은 단순히 삭제한다.

## 실습 1. 리스트에 새로운 요소 삽입하기
```
def solution(L, x):
    # L이 오름차순으로 정렬되어 있다고 가정했으므로 가장 먼저 입력 값(x)을 리스트(L)의 가장 큰 값과 비교한다.
    if L[-1] < x:
        L.append(x)
    else:
        # 입력 값이 리스트의 가장 큰 값보다 작으므로, 리스트를 순회하며 입력 값의 위치를 찾는다.
        for i in range(len(L)):
            if L[i] > x:
                L.insert(i,x)
                break
    return L
```

## 실습 2. 리스트에서 원소 찾아내기
```
def solution(L, x):
    answer, num = [], 0
    # 찾으려는 원소(x)가 리스트(L)에 있나 확인 후, 없으면 [-1]을 반환한다.
    if x not in L:
        return [-1]
    else:
        # 원소가 리스트에 있을 경우, 최대 리스트의 길이만큼 탐색
        for i in range(len(L)):
            if x in L[num:]:
                # 리스트에서 원소를 찾았을 경우, 해당 인덱스를 answer 리스트에 append 한다.
                answer.append(L[num:].index(x)+num)
                # 그리고 변수 num에 인덱스 + 1을 저장해 리스트 슬라이싱에 사용한다.
                num += (L[num:].index(x)+1)
            # 리스트에 더 이상 원소가 없을 경우 for 문을 빠져나가 answer 리스트를 return 한다.
            else:
                break
    return answer
```
