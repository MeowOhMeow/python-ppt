import re

reg = re.compile(r'^[A-Z][1-2]\d{8}$')   # regex
while True:
    idToJudge:str = input()
    if idToJudge == 'Q':    # 跳出
        break
    print(idToJudge, end='')
    print('正確' if reg.search(idToJudge) else '不正確')
