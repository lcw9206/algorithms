'''

LV1. 서울에서 김서방찾기

함수를 완성해서 매개변수 array의 평균값을 return하도록 만들어 보세요.

어떠한 크기의 array가 와도 평균값을 구할 수 있어야 합니다.

'''


# 내 풀이
import numpy


def average(array):
    # 함수를 완성해서 매개변수 array의 평균값을 return하도록 만들어 보세요.
    return numpy.mean(array)


# 아래는 테스트로 출력해 보기 위한 코드입니다.
array = [5,3,4]
print("평균값 : {}".format(average(array)))
