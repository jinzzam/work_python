# input("당신의 이름은?")
name = input("당신의 이름은?")
# birth = input("당신이 태어난 해는?")    #숫자를 입력해도 문자로 받음
birth = int(input("당신이 태어난 해는?"))  

age = 2025 - birth  # 'int' and 'str' => int 로 변환해서 오류 해결
# print("%d님" %name) # 오류 : not str
# print("%s님" %name) # %s 문자열을 받음
# print("%s님이 태어난 해는 %d년 입니다." %(name, birth)) 
# print("%s님이 태어난 해는 %s년입니다." %(name, birth)) 
print("%s의 나이는 %s세 입니다." %(name, age)) 