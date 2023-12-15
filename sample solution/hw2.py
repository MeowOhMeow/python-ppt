import random
# import time

# def cal(k):
#     # 所有真因數中，(本身/2)是最大的。用sum&for迴圈加總所有因數
#     s:int = sum(j for j in range(1, int(k/2)+1) if k % j == 0)
#
#     if s == k:
#         return k
#     else:
#         return 0			# 0 可以讓if不成立
#
#
# n:int = int(input())
#
# # 要使用下面的.join()必須用string，所以將判斷好的完全數轉成string並存在list中
# listOfPerfectNumber:list = [str(i) for i in range(1, n+1) if cal(i)]
#
# if listOfPerfectNumber:
#     print('為完全數\n'.join(listOfPerfectNumber) + '為完全數', end='')

def miller_rabin_primality_test(n): # 有機率出錯
    # 找到一個整數d和一個正整數s，使得n-1可以表示為2^s * d的形式
    s = 0
    d = n - 1
    while d % 2 == 0:
        s += 1
        d //= 2

    # 檢查40次
    for j in range(40): # 提高檢查次數可以降低錯誤率
        # 隨機選擇一個a，其值在[2, n-2]之間
        a = random.randrange(2, n - 2)

        # 計算x
        x = pow(a, d, n)

        # 如果x等於1或等於n-1，則跳過此次循環
        if x == 1 or x == n - 1:
             continue

        # 檢查是否存在一個整數r，使得x^(2^r)等於n-1
        for r in range(1, s):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            # 如果沒有找到，則返回False
            return False
    # 如果所有的檢查都通過了，則返回True
    return True


def isprime(n: int):  # from sympy.isprime()
    if n in [2, 3, 5]:
        return True
    if n < 2 or (n % 2) == 0 or (n % 3) == 0 or (n % 5) == 0:
        return False
    if n < 49:  # 49內質數一定可以由2, 3, 5判斷出來，但49不行
        return True
    if (n % 7) == 0 or (n % 11) == 0 or (n % 13) == 0 or (n % 17) == 0 or \
            (n % 19) == 0 or (n % 23) == 0 or (n % 29) == 0 or (n % 31) == 0 or \
            (n % 37) == 0 or (n % 41) == 0 or (n % 43) == 0 or (n % 47) == 0:
        return False
    if n < 2809:
        return True
    if n <= 23001:  # 我也不知道是甚麼
        return pow(2, n, n) == 2 and n not in [7957, 8321, 13747, 18721, 19951]
    return miller_rabin_primality_test(n)

def perfect_num(k, num):
    return 2 ** (k - 1) * num  # 2^(n-1)x(2^n-1)是完全數 by wiki


def mersenne_num(prime_number):
    return 2 ** prime_number - 1  # 他的公式


user_input = int(input())
# start = time.perf_counter_ns()
i = 0
previous_value = 0
while True:
    i += 1

    if not isprime(i):              # 如果不是質數
        continue

    # 是質數:
    next_value = mersenne_num(i)    # n 為質數的梅森數
    if not isprime(next_value):     # 如果不是梅森質數
        continue

    # 是梅森質數:
    if previous_value != 0:         # 為了避免多印一行的奇怪操作
        print(str(previous_value) + '為完全數', end='')
    next_value = perfect_num(i, next_value)

    if next_value <= user_input:    # 如果下一個值小於使用者輸入
        if previous_value != 0:     # 不是第0個值才換行
            print()
        previous_value = next_value # 經過這後回到上面，又是梅森質數的時候就能印出了
    else:
        break

# end = time.perf_counter_ns()
# print()
# print('運行時間: ', end - start, "ns")
