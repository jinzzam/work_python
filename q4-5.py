str = input("문장을 입력해 주세요 : ")
index = len(str)-1
while index>=0:
    if(str[index]==" "):
        print("-",end="")
    else :
        print(str[index], end="")
    index-=1