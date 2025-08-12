import os

if os.path.exists("scores2.txt"):
    os.remove("scores2.txt")    #파일이 존재하면 삭제
else:
    print("파일이 존재하지 않음!")