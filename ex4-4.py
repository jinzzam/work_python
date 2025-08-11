for i in range(1, 11): 
    print(i, end=" ")   #end : 엔터 대신에 스페이스로 출력됨
    # print(i, end="777")   #end : 엔터 대신에 777로 출력됨
print('')   # 작은 따옴표 줄바꿈
print("")   # 큰 따옴표 줄바꿈
print()     # 공백

# 초기값 : 0, 10-1까지 반복
for i in range(10): 
    print(i, end=" ") 
print()
for i in range(1,10,2):   #2씩 증가
    print(i, end=" ") 
print()
for i in range(20, 0, -2):   #2씩 감소 2까지 출력
# for i in range(20, -1, -2):   #2씩 감소 0까지 출력
    print(i, end=" ") 