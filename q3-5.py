a = int(input("첫 번째 정수는 ? "))
b = int(input("두 번째 정수는 ? "))
c = int(input("세 번째 정수는 ? "))

# if a>b :
#     max = a
# if c>max :
#     max = c
# if a>max :
#     max = a
# if b>max:
#     max = b

# print("%d, %d, %d중에서 가장 큰 수는 %d입니다." %(a, b, c, max))

if a>b and a>c :
    largest = a
elif b>a and b>c :
    largest = b
else :
    largest = c
    
print("%d, %d, %d중에서 가장 큰 수는 %d입니다." %(a, b, c, largest))