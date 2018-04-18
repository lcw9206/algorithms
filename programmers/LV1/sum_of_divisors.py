'''

LV1. 약수의 합

어떤 수를 입력받아 그 수의 약수를 모두 더한 수 sumDivisor 함수를 완성해 보세요.

예를 들어 12가 입력된다면 12의 약수는 [1, 2, 3, 4, 6, 12]가 되고, 총 합은 28이 되므로 28을 반환해 주면 됩니다.

'''


# 내 풀이
def sum_divisor(num):
    answer = 0
    for i in range(1, (num // 2) + 1):
        if num % i == 0:
            answer += i

    answer += num
    return answer


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(sum_divisor(12))


# 하고자 했던 풀이

def sum_divisor(num):
    answer=0
    return num + sum([i for i in range(1, (num//2)+1) if num % i == 0])


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(sum_divisor(12))
