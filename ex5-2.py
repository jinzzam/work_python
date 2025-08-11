color = ["빨강","주황","노랑","초록","파랑","남색","보라"]



print("color[0] : ",color[0])
print("color[5] : ",color[5])
print("color[2:6] : ",color[2:6])   #2~5
print("color[-3] : ",color[-3])    #뒤에서 3번째 '파랑'  
print("color[-4:-1] : ",color[-4:-1])    # '초록' '파랑' '남색'

for co in color : 
    # print(co)
    print("나는 %s을 좋아한다."%co)

n = len(color)
# print(n)    # 7

for i in range(0, n):
    print(i)    # 0~6 
    print("나는 %s을 좋아한다."%color[i])