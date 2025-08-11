string1 = "Python is fun!"
print(string1)

# x = string1.find("fun")
# print(x)    # fun이 시작하는 곳의 인덱스

x = string1.replace("fun", "nice")
print(x)    

list1 = string1.split(" ")
print(list1)
print(type(list1))  #<class 'list'>

for i in range(0, len(list1)):
    print("list[%d] : %s"%(i, list1[i]))

