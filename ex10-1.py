# f = open("new_file.txt","w", encoding="utf-8")
# f = open("new_file2.txt","w", encoding="utf-8")
# f = open("new_file3.txt","w", encoding="utf-8")
f = open("new_file.txt","a", encoding="utf-8") # a모드 : 기존 파일에 내용 추가
# names=["홍지수","안지영","김연수","김예린","한정연"]
names=["손영민","황현준"]

for name in names:
    f.write(name+"\n")

print("파일쓰기 완료!")

f.close()