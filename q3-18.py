start = int(input("시작 수는? "))
end = int(input("끝 수는? "))
num = int(input("정수를 입력하세요 :  "))
if num>start and num<end:
    print("%d는 %d~%d 사이에 있다."%(num,start,end))
else:
    print("%d는 %d~%d 사이에 없다."%(num,start,end))