fruits = ["apple","orange","banana","cherry"]
# print(fruits)

fruits.insert(1, "melon")
print(fruits)

fruits.insert(2, "strawberry")
print(fruits)

idx = fruits.index("banana")
print(idx)  #2

fruits.remove("banana")
print(fruits)