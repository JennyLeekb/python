"""
输入两个正整数计算最大公约数和最小公倍数

Author: lkb
"""

x = int(input('请输入第一个正整数：'))
y = int(input('请输入第二个正整数：'))

if x > y:
    x,y = y,x

# // 表示整数除法 / 表示浮点除法
for factor in range(x,0,-1):
    if x%factor==0 and y%factor==0:
        print('%d和%d的公约数是：%d'%(x,y,factor))
        print('%d和%d的公倍数是：%d'%(x,y, x*y // factor))
        break