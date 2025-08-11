car={"brand":"현대", "model":"아반떼", "start":1990, "year":"2021"}
print(car)

x= car.pop("start") # pop : 키에 해당되는 값(잘라내기)
print(x)
print(car)

car.clear() # 키와 값을 모두 삭제
print(car)