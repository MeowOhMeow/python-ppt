import datetime

array_length = int(input())
# python 沒有的enum(要用模組)，用tuple其實是同個意思
weekday_enum: tuple = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')

for i in range(array_length):
    # date, days = input().split(',')
    # date = datetime.datetime.strptime(date, '%Y-%m-%d') + datetime.timedelta(days=int(days))
    # print(date.strftime('%Y-%m-%d(%a)'), end='')
    # if i < array_length - 1:
    #     print()

    date, days = input().split(',')     # date 存日期，days存要加的天數
    # let input = 2022-1-1,3
    # input().split() = ['2022-1-1', '3']
    # date = '2022-1-1'
    # days = '3'

    date = date.split('-')         # 變成list
    # date = ['2022', '1', '1']

    # 變成datatime.date 物件
    date = datetime.date(int(date[0]), int(date[1]), int(date[2]))
    # datetime.date 要三個參數(year, month, date)
    # 這裡的date 變成datetime module 裡面的 object，代表2022/1/1

    # 加法
    date = date + int(days) * datetime.date.resolution
    # datetime.date.resolution 是datetime裡面的一天
    # https://docs.python.org/3.10/library/datetime.html#datetime.resolution

    # datetime.date().weekday() 會回傳 0~6，代表星期一到日，我用tuple去索引後面的文字，例：weekday_enum[0] == 'Mon'
    print(date, f'({weekday_enum[date.weekday()]})', sep='', end='')

    if i < array_length - 1:
        print()
