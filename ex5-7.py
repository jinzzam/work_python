scores = [80, 90, 85, 95, 100]

# s = sum(scores)
# avg = s/len(scores)
# print("합계 : ", s)
# print("평균 : ", avg)

# scores.reverse()  # 배열 순서 완전히 반대로 정렬
# print(scores)

# x = scores.copy()   # 리스트 복사
# print(x)
# print(scores)

scores.sort()   # ascending
print(scores)

scores.sort(reverse=True)   # decending
print(scores)