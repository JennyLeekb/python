"""
输入半径计算圆的周长和面积


author: lkb
"""

import math

r = float(input('请输入半径： '))
l = 2 * math.pi * r
s = math.pi * r * r

print('周长是 %.3f ' % l)
print('面积是 %.3f ' % s)