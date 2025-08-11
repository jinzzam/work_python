def sum_tuple(tup):
    sum=0
    for a in range(len(tup)):
        sum+=tup[a]
    return sum
tup1=(10, 20, 30, 40, 50)
print("튜플의 합계 : %d"%sum_tuple(tup1))