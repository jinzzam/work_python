# a = float(input("등급을 입력하세요 : "))
# if a==4.5:
#     print("등급 : A+, 평점 : %.1f"%a)
# elif a>=4.0:
#     print("등급 : A, 평점 : %.1f"%a)
# elif a>=3.5:
#     print("등급 : B+, 평점 : %.1f"%a)
# elif a>=3.0:
#     print("등급 : B, 평점 : %.1f"%a)
# elif a>=2.5:
#     print("등급 : C+, 평점 : %.1f"%a)
# elif a>=2.0:
#     print("등급 : C, 평점 : %.1f"%a)
# elif a>=1.5:
#     print("등급 : D+, 평점 : %.1f"%a)
# elif a>=1.0:
#     print("등급 : D, 평점 : %.1f"%a)
# elif a>=0:
#     print("등급 : F, 평점 : %.1f"%a)
# else :
#     print("error")


a = input("등급을 입력하세요(A+,A,B+...F) : ")
if a=="A+":
    print("등급 : %s, 평점 : 4.5"%a)
elif a=="A":
    print("등급 : %s, 평점 : 4.0"%a)
elif a=="B+":
    print("등급 : %s, 평점 : 3.5"%a)
elif a=="B":
    print("등급 : %s, 평점 : 3.0"%a)
elif a=="C+":
    print("등급 : %s, 평점 : 2.5"%a)
elif a=="C":
    print("등급 : %s, 평점 : 2.0"%a)
elif a=="D+":
    print("등급 : %s, 평점 : 1.5"%a)
elif a=="D":
    print("등급 : %s, 평점 : 1.0"%a)
elif a=="F":
    print("등급 : %s, 평점 : 0"%a)