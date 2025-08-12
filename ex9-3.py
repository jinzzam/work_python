import math

print("sin(2) : ", math.sin(2))
print("cos(2) : ", math.cos(2))
print("tan(2) : ", math.tan(2))
print("ceil(12.3) : ", math.ceil(12.3)) # 13 올림
print("floor(12.3) : ", math.floor(12.3)) # 12 내림
print("round(12.3) : ", round(12.3)) # 12 반올림

print(math.fsum([1, 2, 3, 4, 5]))   # 리스트 합계
print(math.fsum([1.7, 2.3, 3.5, 4, 5]))   # 리스트 실수 합계
print(math.fsum((10, 20, 30, 40, 50)))   # 튜플 합계

print("log(75.3) : ", math.log(75.3))
print("pow(5, 2) : ", math.pow(5, 2))
print("sqrt(25) : ", math.sqrt(25))