def average(*args):
    # print(args)     # 여러 개의 값의 출력이 튜플 형식(85, 96, 87)
    num_args = len(args)
    sum=0
    for i in range(num_args):
        sum+=args[i]
    # print(sum)
    avg = sum/num_args
    # print(avg)
    print("%d과목 평균 : %.1f"%(num_args, avg))
average(85, 96, 87)
average(85, 96, 87, 77, 34, 98)
average(1)