def str_hypen(string):
    result = "" 
    for s in string:
        if(s==" "):
            s='-'
        result+=s
    return result

string=input("문자열을 입력하세요 : ")
print(str_hypen(string))


def space_hyphen(string):
    result=""
    i=0

    while i<len(string):
        if string[i] == " ":
            result+="-"
        else:
            result+=string[i]
        i+=1
    return result
string=input("문자열을 입력하세요 : ")
print(space_hyphen(string))