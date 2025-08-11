def kilo_mile(k):
    return k*0.621371

kilo = int(input("킬로미터를 입력하세요 : "))
mile = kilo_mile(kilo)

print("%d 킬로미터는 %.2f 마일이다."%(kilo, mile))