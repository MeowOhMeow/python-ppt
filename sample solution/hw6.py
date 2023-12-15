# def cal1(col):
#     tempList:list = []  # 用來存符合條件學生的list
#     passNumber:int = 0  # 符合條件的學生數
#
#     for i in studentList:  # 訪問所有元素(list)
#         tempList2:list = []  # 臨時陣列，如果符合條件會用來存學號、姓名，最後加到tempList的尾端
#         if int(i[col]) >= 60:  # i[2]是國文成績，假設60分及格
#             tempList2.append(i[0])
#             tempList2.append(i[1])
#             tempList.append(tempList2)
#
#             passNumber += 1
#     return tempList, passNumber
#
# def cal2():
#     tempList:list = []
#     passNumber:int = 0
#     for i in studentList:
#         tempList2:list = []
#         if int(i[2]) >= 60 and int(i[3]) >= 60:  # 同時及格
#             tempList2.append(i[0])
#             tempList2.append(i[1])
#             tempList.append(tempList2)
#
#             passNumber += 1
#     return tempList, passNumber
#
# def cal3():
#     tempList: list = []
#     failNumber: int = 0  # failNumber比較符合意義
#     for i in studentList:
#         tempList2: list = []
#         if int(i[2]) < 60 and int(i[3]) < 60:
#             tempList2.append(i[0])
#             tempList2.append(i[1])
#             tempList.append(tempList2)
#
#             failNumber += 1
#     return tempList, failNumber
#
#
#
# studentList:list = []
# while True:
#     s:str = input()
#     if s == 'Q':
#         break
#     studentList.append(s.split(','))  # 跟讀.csv檔時一樣，用split拆分資料，split會回傳一個list
#
# studentList.sort()
# print(studentList)
#
# totalStudent:int = len(studentList)  # 總人數
#
# temp:tuple = cal1(2)
# print(temp[0])
# print('國文成績及格比率為' + str(int(temp[1] / totalStudent * 100)) + '%')
#
# temp:tuple = cal1(3)
# print(temp[0])
# print('數學成績及格比率為' + str(int(temp[1] / totalStudent * 100)) + '%')
#
# temp:tuple = cal2()
# print(temp[0])
# print('兩科成績及格比率為' + str(int(temp[1] / totalStudent * 100)) + '%')
#
# temp:tuple = cal3()
# print(temp[0])
# print('兩科成績不及格比率為' + str(int(temp[1] / totalStudent * 100)) + '%')


class Student:          # 定義class
    def __init__(self, studentId, name, chinese, math):
        self.id = studentId
        self.name = name
        self.chinese = chinese
        self.math = math

    def get_id(self):
        return self.id

    def get_info(self):
        return [self.id, self.name, self.chinese, self.math]

    def get_id_and_name(self):
        return [self.id, self.name]

    def is_pass(self, option):  # 回傳bool
        if option == 2:
            return int(self.chinese) >= 60
        elif option == 3:
            return int(self.math) >= 60
        else:
            raise KeyError      # 使用錯誤的key會拋出error，如果沒有except KeyError{}會中斷執行

def print_student():
    tempList:list = []
    for i in studentList:
        tempList.append(i.get_info())
    print(tempList)

def cal(option):
    tempList: list = []
    number: int = 0
    for student in studentList:
        if option == 1 and student.is_pass(option=2):  # 國文成績及格
            tempList.append(student.get_id_and_name())
            number += 1
        elif option == 2 and student.is_pass(option=3):  # 數學成績及格
            tempList.append(student.get_id_and_name())
            number += 1
        elif option == 3 and student.is_pass(option=2) and student.is_pass(option=3):   # 兩科都及格
            tempList.append(student.get_id_and_name())
            number += 1
        elif option == 4 and not student.is_pass(option=2) and not student.is_pass(option=3): #兩科都不及格
            tempList.append(student.get_id_and_name())
            number += 1

    print(tempList)
    if option == 1:
        print('國文成績及格比率為' + str(int(number / totalStudent * 100)) + '%')
    elif option == 2:
        print('數學成績及格比率為' + str(int(number / totalStudent * 100)) + '%')
    elif option == 3:
        print('兩科成績及格比率為' + str(int(number / totalStudent * 100)) + '%')
    elif option == 4:
        print('兩科成績不及格比率為' + str(int(number / totalStudent * 100)) + '%', end='')
    else:
        raise KeyError
    return

def input_students():
    while True:
        s = input()
        if s == 'Q':
            break
        s = s.split(',')
        tempStudent = Student(s[0], s[1], s[2], s[3])
        studentList.append(tempStudent)  # 跟讀.csv檔時一樣，用split拆分資料，split會回傳一個list

if __name__ == '__main__':
    studentList: list = []
    input_students()
    # 這裡的key使用lambda匿名函式排序：studentList[0]會用studentList[0].get_id()的值進行排序
    studentList.sort(key=lambda x: x.get_id())
    print_student()
    totalStudent:int = len(studentList)  # 總人數

    cal(1)
    cal(2)
    cal(3)
    cal(4)
