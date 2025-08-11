# def func(n):  
def func():  
    # x=n+5
    # print(x)
    # return x
    #global x  # 컴파일(?) 할 때 얘 인식 못하나?
    x=100   # 지역변수 : 함수 내에서만 사용 가능
    print(x)

# func(10)
# a = func(10)    # 리턴값이 없을 때 None
# print(a)
x=200
print(x)
func()
print(x)
# 200
# 100
# 200

# global x 적용후
# 200
# 100
# 100