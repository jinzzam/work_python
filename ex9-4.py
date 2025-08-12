import time

seconds = time.time()
# 그리니치 천문대 기준으로 1970년 1월1일0시0분0초부터 경과된 시간(ms)
print(seconds)

tm = time.gmtime()
print(tm)

tm2 = time.localtime(1754966043.7085998)
print("년 : ",tm2.tm_year)
print("월 : ",tm2.tm_mon)
print("일 : ",tm2.tm_mday)
print("시 : ",tm2.tm_hour)
print("분 : ",tm2.tm_min)
print("초 : ",tm2.tm_sec)