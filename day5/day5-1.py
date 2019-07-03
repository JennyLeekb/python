"""
寻找水仙花数
水仙花数是指一个 3 位数，它的每个位上的数字的 3次幂之和等于它本身（例如：1^3 + 5^3+ 3^3 = 153）。

Author: lkb
"""

from math import pow


for num in range(100,999):
    x = num%10
    y = num%100//10
    z = num//100
    if(pow(x,3) + pow(y,3) + pow(z,3)) == num:
        print('%d num是水仙花数' % num)