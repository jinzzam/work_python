numbers = [7, 9, 15, 18, 30, -3, 7, 12, -16, -12]

sum=0
i = 0
list_even = []
while i<len(numbers):
    if(i%2!=0):
        list_even.append(numbers[i])
        sum += numbers[i]
    i+=1
print("짝수 번째 요소 : ", list_even)
print("합계 : ",sum)