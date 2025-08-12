class Members:
    total = 0   # 클래스 속성

    def __init__(self, name, phone):  # 생성자
        self.name=name  # 객체 속성
        self.phone=phone  
        Members.total += 1
        # self.total += 1
    def show_info(self):
        print("이름 : %s, 전화번호 : %s"%(self.name, self.phone))
        

member1 = Members("황선영","010-2222-1234") 
member2 = Members("강동욱","010-3333-1234") 
member3 = Members("신진서","010-4444-1234") 

member1.show_info()
member2.show_info()
member3.show_info()

# print("총 회원 수 : ",member1.total)
# print("총 회원 수 : ",member3.total)
print("총 회원 수 : ", Members.total)
# print("총 회원 수 : ", member3.total)