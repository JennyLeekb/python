"""
写一个程序判断输入的正整数是不是回文素数

Author:lkb
"""


def is_palindrome(num):
    temp = num 
    total = 0
    while temp > 0 :
        total = total * 10 + temp%10
        temp //= 10
    return total == num


def is_prime(num):
    for x in range (2,num):
        if num % x == 0:
            return False
    return True



if __name__ == '__main__':
    num = int(input('请输入正整数: '))
    if is_palindrome(num) and is_prime(num):
        print('%d是回文素数' % num)
    else:
        print('%d不是回文素数' % num)
