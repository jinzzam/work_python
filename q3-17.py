print("기능 선택")
print("1. 더하기")
print("2. 빼기")
print("3. 곱하기")
print("4. 나누기\n")

cal = input("계산기 기능을 선택하세요(1/2/3/4) : ")

a = int(input("첫 번째 숫자를 입력하세요 : "))
b = int(input("두 번째 숫자를 입력하세요 : "))

if(cal=='1'):
    x = a+b
    print("%d + %d = %d"%(a, b, x))
elif(cal=='2'):
    x = a-b
    print("%d - %d = %d"%(a, b, x))
elif(cal=='3'):
    x = a*b
    print("%d * %d = %d"%(a, b, x))
elif(cal=='4'):
    x = a/b
    print("%d / %d = %.2f"%(a, b, x))
else:
    print("선택 오류!")

# print("%d %s %d = %d"%(a, cal, b, x))