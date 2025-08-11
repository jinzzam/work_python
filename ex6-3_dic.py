member={"name":"황예린", "age":22, "email":"yerin@hanmail.net"}
print(member)

# 리스트, 튜플을 사용해서 딕셔너리를 생성
score = dict([("국어", 80), ("영어", 90), ("수학", 100)])
print(score)
print(score["국어"])    # 키를 사용해서 값을 출력
print(score["영어"])
print(score["수학"])

score["음악"]=70    # 없는 키는 추가
print(score)

score["수학"]=77    # 있는 키는 값을 변경
print(score)