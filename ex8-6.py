class Person:
    def __init__(self, name):
        # pass    # 동작 없이 다음 실행
        self.name = name
    def show_name(self):
        print(self.name)

class Student(Person):  #Person 클래스(부모)를 상속받는 Student 클래스(자식)
    pass

# TypeError: Person.__init__() missing 1 required positional argument: 'name'
# x = Student()
x = Student("홍길동")
x.show_name()