def divide(a, b):
    try:
        c=a/b
    except ZeroDivisionError:   #분모 0일때
        print("0 나누기 오류가 발생함!")
    # finally:  # 무조건 실행
    else:   # 경우에 따라 실행시키고 싶을 때
        print(c)

divide(30, 10)
# divide(30, 0)