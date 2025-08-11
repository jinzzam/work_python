def int_to_zz(n):
    result = []
    i=1
    while i <= n:
        result.append(i*i)  # i**2 : i의 제곱의 다른 표현
        i+=1
    return result

n=int(input("n값을 입력하세요 : "))
print(int_to_zz(n))