write = int(input("필기시험 점수는?"))
do = int(input("실기시험 점수는?"))
result="불합격"
if write>=80 and do>=80 :
    result="합격"
print("- 필기시험 점수 : %d"%write)
print("- 실기시험 점수 : %d"%do)
print("- 판정 : %s"%result)