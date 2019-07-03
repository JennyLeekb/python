"""
寻找完美数
它所有的真因子（即除了自身以外的约数）的和（即因子函数），恰好等于它本身。如果一个数恰好等于它的因子之和，则称该数为“完全数”。

Author: lkb
"""
from math import sqrt

for num in range(1,10000):
    sum = 0
    for x in range(1, num//2+1):
        if num % x == 0:
            sum += x
    if(sum == num):
        print('%d 是完全数'%num)
