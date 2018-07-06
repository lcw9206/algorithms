## 정렬 (Sort)
* 배열 안의 원소들을 정해진 기준에 따라 새로 늘어놓는 것

## 정렬과 관련된 함수들
### 1. sorted()
> * 내장 함수
> * 정렬된 새로운 리스트를 얻어낸다.

### 2. sort(L)
> * 리스트의 메서드
> * 해당 리스트(L)를 정렬한다.

### sorted(), sort()의 차이점은?
> sorted()는 정렬된 리스트를 받을 변수가 필요하며 해당 리스트는 변화가 없고, sort()는 해당 리스트가 정렬된다.
```
L = [3, 4, 2, 5]
L2 = sorted(L)
>>> L = [3, 4, 2, 5] , L2 = [2, 3, 4, 5]

L.sort()
>>> L = [2, 3, 4, 5]

'''두 메서드의 인자로 reverse=True를 추가하면 역순으로 정렬이 가능하다.'''
```

### 문자열 길이 순서로 정렬하려면 어떻게 해야할까?
> 정렬에 이용하는 key를 lambda 함수를 이용해 지정한다.
```
1. 문자열 길이 순서로 정렬

L = ['abcd', 'xyz', 'spam']
sorted(L, key=lambda x: len(x))
>>> ['xyz', 'abcd', 'spam']

2. 원소들의 이름 순서대로 정렬

L = [{'name':'Paul', 'score':83},
     {'name':'John', 'score':92}]
L.sort(key=lambda x: x['name'])
>>> [{'name':'John', 'score':92},
     {'name':'Paul', 'score':83}]
```
