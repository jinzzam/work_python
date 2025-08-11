phone_list1 = ["010-1111-2222","010-2222-3333","010-4444-5555"]
print(phone_list1)

phone_list2 = []
for number in phone_list1:
    # print(number)
    x = number.replace("-", "")
    phone_list2.append(x)

print(phone_list2)