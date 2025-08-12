class Members:
    def __init__(self, name, age):  # 생성자
        self.name=name 
        self.age=age  
    def show_info(self):
        print("이름 : ",self.name)
        print("나이 : ",self.age)

# TypeError: Members.__init__() missing 2 required positional arguments: 'name' and 'age'
# member1 = Members() 
member1 = Members("황선영",18) 
member1.show_info()
member2 = Members("최종화",32) 
member2.show_info()