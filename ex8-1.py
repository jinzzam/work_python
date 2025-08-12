class Person:   # 사람이나 사물이 될 수 있는 틀/판
    name="김정연"   #name : 속성
    # person1 객체를 self 가 받음
    def hello(self):    # 객체를 self 로 받음 : 파이썬에 있는 내용임
        print(Person.name + "님 안녕하세요")

person1 = Person()    #객체 생성
person1.hello()     #메소드 호출

Person.name="황서영"
person1.hello()     #메소드 호출
