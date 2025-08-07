tel = input("하이픈(-)이 포함된 11자리의 휴대폰 번호는?")
print("- 입력된 휴대폰 번호 : %s" %tel)
tel2 = tel[0:3]+tel[4:8]+tel[9:]
print("- 하이픈 삭제된 휴대폰 번호 : " + tel2)
[a, b, c]=tel.split('-')
num = a+b+c
print("- 하이픈 삭제된 휴대폰 번호 : " + num)