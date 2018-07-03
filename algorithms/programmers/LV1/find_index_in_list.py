'''

LV1. 서울에서 김서방찾기

findKim 함수(메소드)는 String형 배열 seoul을 매개변수로 받습니다.

seoul의 element중 Kim의 위치 x를 찾아, 김서방은 x에 있다는 String을 반환하세요.

seoul에 Kim은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.

'''


# 내 풀이
def find_kim(seoul):
    kim = list(seoul)
    kim_idx = kim.index('Kim')
    return "김서방은 {}에 있다".format(kim_idx)


# 실행을 위한 테스트코드입니다.
print(find_kim(["Queen", "Tod", "Kim"]))


# 가장 좋은 풀이
def find_kim(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))

# 실행을 위한 테스트코드입니다.
print(find_kim(["Queen", "Tod", "Kim"]))
