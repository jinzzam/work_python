f = open("new_file.txt","r", encoding="utf-8") # a모드 : 기존 파일에 내용 추가
lines = f.readlines()   # readlines : 전체 내용을 읽어 옴

for line in lines:
    temp = line.replace("\n", "")
    print(temp)

print("파일 읽기 완료!")

f.close()