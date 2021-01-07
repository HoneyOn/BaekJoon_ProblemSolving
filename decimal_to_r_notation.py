def decimal_to_r_notation(number, r):
    """10진수를 입력받아 r진수(r=2,8,16...)로 변환하는 함수"""
    number_front = int(number)
    number_rear = number - number_front

    ###정수 부분 r 진수 변환
    #n을 r로 나눈 나머지를 담는 list
    remainder_list = []
    
    while True:
        #divmod(n, r)은 n을 r로 나눈 값을(몫, 나머지) tuple로 반환
        quotient = divmod(number_front, r)[0]
        remainder = divmod(number_front, r)[1]
        remainder_list.append(remainder)
        #몫이 0이면 반복문 탈출
        if quotient ==0: break
        else:
            number_front = quotient
    
    #remainder_list 원소 배열 순서를 거꾸로 뒤집는다
    remainder_list.reverse()
    result_front = ""
    for digit in remainder_list:
        result_front += str(digit)

    ###소수 부분 r 진수 변환
    #소수 부분에 r을 곱한 결괏값 중 정수 부분을 담는 list
    integer_part_list = []

    while True:
        #소수 부분에 r을 곱한 값 중 정수만을 따로 list에 담는다. 소수부가 0될때까지 반복
        integer_part = int(number_rear*r)
        decimal_part = number_rear*r - integer_part
        integer_part_list.append(integer_part)
        if decimal_part ==0: break
        else:
            number_rear = decimal_part

    result_rear=""
    for digit in integer_part_list:
        result_rear += str(digit)

    return result_front+"."+result_rear

print(decimal_to_r_notation(100,16))
