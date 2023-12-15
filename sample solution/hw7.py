array_length: int = int(input())    # 資料數

for i in range(array_length):
    have_digit: bool = False        # 預設為 False
    have_alpha: bool = False
    length_level: int = 0           # 長度等級

    pwd = input()
    for temp in pwd:                # loop string 中每一個字元
        if temp.isdigit():          # 有遇到 digit 就設為 True
            have_digit = True
        if temp.isalpha():
            have_alpha = True
    if len(pwd) >= 6:               # 1
        length_level += 1
    if len(pwd) >= 10:              # 2
        length_level += 1

    if length_level == 0:
        print(f'{pwd}不安全的密碼', end='')
    elif have_digit and have_alpha and length_level == 2:
        print(f'{pwd}非常安全的密碼', end='')
    elif have_digit and have_alpha and length_level == 1:
        print(f'{pwd}安全的密碼', end='')
    else:                           # length_level = 1~2; have_digit, have_alpha 擇一
        print(f'{pwd}可能是安全的密碼', end='')

    if i < array_length-1:          # 不是最後一筆資料就換行
        print()
