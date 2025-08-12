class Sadari:
    def __init__(self, down, up, height):
        self.down=down
        self.up=up
        self.height = height
    def area(self):
        a = (self.down+self.up)/2 * self.height
        print("사다리꼴의 면적 : %.2f"%a)
        

downside=int(input("밑변의 길이를 입력하세요 : "))
upside=int(input("윗변의 길이를 입력하세요 : "))
height=int(input("높이를 입력하세요 : "))
s1 = Sadari(downside, upside, height)
s1.area()