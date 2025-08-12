class Members:
    def set_info(self, name):
        self.name=name  # self.name : 객체의 속성
        print(name)
    def show_info(self):
        print("이름 : ",self.name)

member1 = Members()      #객체 생성
member1.set_info("홍지수")

member2 = Members()      #객체 생성
member2.set_info("안지영")

member1.show_info()
member2.show_info()