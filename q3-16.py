a = int(input("첫 번째 숫자를 입력하세요 : "))
b = int(input("두 번째 숫자를 입력하세요 : "))
cal = input("원하는 연산은?\n+,-,*,/ 중 하나를 선택하세요 : ")

if(cal=='+'):
    x = a+b
    print("%d %s %d = %d"%(a, cal, b, x))
elif(cal=='-'):
    x = a-b
    print("%d %s %d = %d"%(a, cal, b, x))
elif(cal=='*'):
    x = a*b
    print("%d %s %d = %d"%(a, cal, b, x))
elif(cal=='/'):
    x = a/b
    print("%d %s %d = %.2f"%(a, cal, b, x))
else:
    print("선택 오류!")

# print("%d %s %d = %d"%(a, cal, b, x))