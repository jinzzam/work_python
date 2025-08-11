animals=("토끼","거북이","사자","여우") #튜플
print(animals)

# TypeError: 'tuple' object does not support item assignment
# 튜플에서 값 변경 불가
# animals[2] = "호랑이"
# print(animals)

# numbers = tuple(range(10))  # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# print(numbers)
numbers = tuple(range(10, 21))  # (10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
print(numbers)

print("numbers[0]=",numbers[0]) # 10
print("numbers[2:5]=",numbers[2:5]) # (12, 13, 14)
print("numbers[2:]=",numbers[2:]) # (12, 13, 14, 15, 16, 17, 18, 19, 20)
print("numbers[:5]=",numbers[:5]) # (10, 11, 12, 13, 14)
print("numbers[-2]=",numbers[-2]) # 19
# ::-1 => 맨 뒤에서 맨 앞으로 출력
print("numbers[::-1]=",numbers[::-1]) # (20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10)