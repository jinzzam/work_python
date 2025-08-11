# def reverse_str(str):
#     str.sort(reverse=True)
#     return str

# str=input("문자열을 입력하세요 : ")
# print(reverse_str(str))


def str_reverse(string):
    result = "" 
    index = len(string)

    while index > 0:
        result += string[index-1]
        index -=1
    return result

string=input("문자열을 입력하세요 : ")
print(str_reverse(string))

# list = "string".split('')
# print(list)