'''

LV1. 자릿수 더하기

sum_digit함수는 자연수를 전달 받아서 숫자의 각 자릿수의 합을 구해서 return합니다.

예를들어 number = 123이면 1 + 2 + 3 = 6을 return하면 됩니다.

sum_digit함수를 완성해보세요.

'''


# 내 풀이
def sum_digit(number):
    return sum([int(i) for i in list(str(number))])


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(sum_digit(123)));


# 다른 풀이
def sum_digit(number):
    return sum([int(i) for i in list(str(number))])


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(sum_digit(123)));


# 다른 풀이2

def sum_digit(number):
    return sum(map(int,str(number)))


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(sum_digit(123)));
