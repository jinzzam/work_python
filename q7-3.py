def count(string, letter):
    cnt=0
    for x in string:
        if x == letter :
            cnt+=1
    return cnt

str = input("영어 문장을 입력하세요:")
letter = input("알파벳 하나를 입력하세요:")
print("%s에 포함된 %s의 개수는 %d개이다."%(str, letter, count(str, letter)))