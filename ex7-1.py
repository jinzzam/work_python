# 매개변수 : 없음, 반환값 : 없음
# def hello():
# def hello(name): # name : 매개변수, 파라미터, 아규먼트, 인자값
def hello(first_name, last_name): # name : 매개변수, 파라미터, 아규먼트, 인자값
    # print("안녕하세요")
    # print("%s님 안녕하세요"%name)
    name = first_name+last_name
    print("이름 : ",name)
# TypeError: hello() missing 1 required positional argument: 'name'
# hello()
# hello("홍지수")
# hello("안지영")
# hello("황예린")
hello("정원", "홍")

