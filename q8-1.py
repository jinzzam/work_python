class Triangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        a = (self.width * self.height)/2
        print("삼각형의 면적 : %.2f"%a)
        

width=int(input("삼각형 밑변의 길이를 입력하세요 : "))
height=int(input("삼각형 높이를 입력하세요 : "))
tri1 = Triangle(width, height)
tri1.area()