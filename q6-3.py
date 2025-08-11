temp= {"월":15.5 ,"화":17.0 ,"수":16.2 ,"목":12.9 ,"금":11.0 ,"토":10.5 ,"일":13.3 }

min="월"
for key in temp:
    if temp[key] < temp[min]:
        min = key
    
print("요일 : %s, 최저 기온 : %.1f"%(min, temp[min]))    
