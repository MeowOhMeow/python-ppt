import re

number:int = int(input())    # 總數
phoneNumbers:list = []

# 輸入電話號碼
for i in range(number):
    phoneNumbers.append(input())

# 用"|"(或)在多個regex中間，表示成單一regex
# r''是指raw string 在''中的特殊符號不會被處理，例如跳脫字元\
reg = r'^(?!(0){2})^0[0-9]{1}-\d{3,4}-\d{4}$|^(?!(0){3})^0[0-9]{2}-\d{2,3}-\d{4}$|^(?!(0){4})^0[0-9]{3}-\d{3}-\d{3}$'

# Compile the regular expression
regex = re.compile(reg)

# 驗證號碼是否正確
for i in range(number):
    if regex.search(phoneNumbers[i]):
        print(phoneNumbers[i], '正確', sep='', end='')
    else:
        print(phoneNumbers[i], '不正確', sep='', end='')
    if i < number - 1:       # 如果不是最後一行，換行
        print()
