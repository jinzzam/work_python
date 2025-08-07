a = int(input("첫 번째 숫자를 입력하세요 : "))
b = int(input("두 번째 숫자를 입력하세요 : "))
# c = f"{a/b:.6}"
# c= f"{a/b:.3}"
c = a/b
# print(a, '/', b, '=', c)
# print("%d / %d = %f" %(a, b, c))
print("%d / %d = %.2f" %(a, b, c))