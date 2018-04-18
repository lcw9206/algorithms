'''

LV1. 제일 작은 수 제거하기

rm_small함수는 list타입 변수 mylist을 매개변수로 입력받습니다.

mylist 에서 가장 작은 수를 제거한 리스트를 리턴하고, mylist의 원소가 1개 이하인 경우는 []를 리턴하는 함수를 완성하세요.

예를들어 mylist가 [4,3,2,1]인 경우는 [4,3,2]를 리턴 하고, [10, 8, 22]면 [10, 22]를 리턴 합니다.

'''


# 내 풀이
def rm_small(mylist):
    num = mylist[0]
    if len(mylist) <= 1:
        return []
    for index in mylist:
        if index < num:
            num = index
    mylist.remove(num)
    return mylist


# 실행을 위한 테스트코드입니다.
my_list = [4, 3, 2, 1]
print("결과 {} ".format(rm_small(my_list)))


# min과 index를 알고 생각한 풀이
def rm_small(mylist):
    mylist.pop(mylist.index(min(mylist)))
    return mylist


# 실행을 위한 테스트코드입니다.
my_list = [4, 3, 2, 1]
print("결과 {} ".format(rm_small(my_list)))


# 가장 좋은 풀이 list comprehension
def rm_small(mylist):
    return [i for i in mylist if i > min(mylist)]


# 실행을 위한 테스트코드입니다.
my_list = [4, 3, 2, 1]
print("결과 {} ".format(rm_small(my_list)))