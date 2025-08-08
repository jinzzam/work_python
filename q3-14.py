a = int(input("수를 입력하세요 : "))
     

if a//100 != 0 and a//10 !=0 and a//1 != 0: 
    print("%d은(는) 세 자리 숫자이다."%a)
elif a//10!=0 :
    print("%d은(는) 두 자리 숫자이다."%a)
elif a//1 !=0: 
    print("%d은(는) 한 자리 숫자이다."%a)
elif a<0 or a>999:
    print("오류! %d은(는) 범위(0~999) 이외의 숫자이다."%a)
