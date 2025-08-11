def cal(c, a, b):
    if c == 1:
        return a+b
    elif c==2:
        return a-b
    elif c==3:
        return a*b
    elif c==4:
        return a/b

c = int(input("원하는 연산을 선택하세요(1/2/3/4) : "))
a = int(input("첫번째 숫자를 입력하세요 : "))
b = int(input("두번째 숫자를 입력하세요 : "))
print("%d %d %d"%(a, b, cal(c, a, b)))