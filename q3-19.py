id="admin"
isOk = "콘텐츠를 이용할 수 없습니다!"

q_id = input("아이디는? ")
if q_id == id :
    isOk = "콘텐츠를 이용이 가능합니다!"
else :
    q_level = int(input("회원 레벨은?(1~9) "))
    if q_level>=1 and q_level<=3 :
        isOk = "콘텐츠를 이용이 가능합니다!"
    
print(isOk)