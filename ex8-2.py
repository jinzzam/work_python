class Cat:
    kor_name="로키"
    eng_name="rockey"
    age=2

    def sound(self):
        print("야옹")
    def speed(self):
        print("엄청 빠르다!")

myCat=Cat()
print("한글 이름: ", myCat.kor_name)    # 객체의 속성으로 출력
print("영어 이름: ", myCat.eng_name)    # 객체의 속성으로 출력
print("나이 : ", myCat.age)    # 객체의 속성으로 출력
myCat.sound()   # 객체의 메소드로 출력
myCat.speed()   # 객체의 메소드로 출력
