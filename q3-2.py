# a = int(input("월을 숫자로 입력하세요 : "))
# if a>=3 and a<=5:
#     print("%d월은 봄입니다."%a)
# elif a>=6 and a<=8:
#     print("%d월은 여름입니다."%a)
# elif a>=9 and a<=11:
#     print("%d월은 가을입니다."%a)
# elif a==12 or a==1 or a==2:
#     print("%d월은 겨울입니다."%a)
# else :
#     print("error")
    

month = input("월을 숫자로 입력하세요 : ")
if month == "3" or month == "4" or month == "5" :
    print("%s월은 봄입니다." %month)
if month == "6" or month == "7" or month == "8" :
    print("%s월은 여름입니다." %month)
if month == "9" or month == "10" or month == "11" :
    print("%s월은 가을입니다." %month)
if month == "12" or month == "1" or month == "2" :
    print("%s월은 겨울입니다." %month)