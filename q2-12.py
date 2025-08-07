book = int(input("책 값은?"))
salePercent = int(input("할인율은?"))
delivery = int(input("배송료는?"))

result = book - (book*(10/100)) + delivery
print("책 값 : %d" %book)
print("할인율 : %d" %salePercent)
print("배송료 : %d"%delivery)
print("결제 금액 : %d" %result)