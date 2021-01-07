def binary_to_decimal_with_point(bi_num):
    """정수부분과 소수부분이 함께있는 2진수의 10진수로의 변환"""

    #2진수를 변환할 10진수의 초기값을 0으로 초기화
    decimal_num = 0

    #2진수 입력값_bi_num dmf answkduf ㄴㅅ갸ㅜㅎdmfh qusghks
    #소수점(.)을 기준으로 문자열 분할
    bi_num_str = str(bi_num).split(".")

    #소수점 앞의 정수 부분과, 소수점 뒤의 소수 부분을 구분
    bi_num_str_front = bi_num_str[0]
    bi_num_str_rear = bi_num_str[1]

    #정수 부분 문자열의 각 자릿값에 2의 n제곱 형태로 가중치를 계산하여 합산
    for index, digit in enumerate(bi_num_str_front):
        decimal_num += int(digit)*pow(2,len(bi_num_str_front)-1 -index)

    # 소수 부분 문자열의 각 자릿값에 2의 -n제곱 형태로 가중치를 계산하여 합산
    for index, digit in enumerate(bi_num_str_rear):
        decimal_num += int(digit) * pow(2, -(1+index))

    return decimal_num


print(binary_to_decimal_with_point(1010.101))

