str = input("숫자를 입력하세요 : ")
i=0
count=0
# for i in range(len(str)):
#     if(int(str[i])%2!=0):
#         count+=1
# print("홀수의 개수 : %d개"%count)

for a in str:
    a = int(a)

    if(a%2 == 1):
        count+=1
print("홀수의 개수 : %d개"%count)
