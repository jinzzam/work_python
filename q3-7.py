letter = input("영문 대문자 또는 소문자 하나를 입력하세요 : ")
letter = letter.lower()

if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u" :
    print("%s은(는) 모음이다."%letter)
else : 
    print("%s은(는) 자음이다."%letter)