row = int(input())          # 輸入數量
listOfInput = []

for i in range(row):
    temporaryList = []      # 臨時List，用來儲存要輸入的element
    numberOfElement = int(input())  # 要輸入的element數量
    for j in range(numberOfElement):
        temporaryList.append(int(input()))  # 將輸入的值放進臨時list
    temporaryList.sort()    # 排序
    listOfInput.append(temporaryList)   # 加到要輸出的List

for i in range(row):
    for j in range(len(listOfInput[i])):
        print(listOfInput[i][j], end='')    # 輸出每個元素
        if j < len(listOfInput[i]) - 1:     # 如果還有下個元素，輸出空格
            print(' ', end='')
    if i < row - 1:                         # 空行
        print()
