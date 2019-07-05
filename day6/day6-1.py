"""
实现计算求最大公约数和最小公倍数的函数。

Author:lkb
"""

"""
求最大公约数
"""
def gcd(x,y):
    (x,y) = (y,x) if x > y else (x,y)
    for factor in range(x,0,-1):
        if x%factor == 0 and y%factor == 0:
            return factor


"""
求最大公倍数
"""
def lcm(x,y):
    return x*y // gcd(x,y)

# __name__是Python中一个隐含的变量它代表了模块的名字
# 只有被Python解释器直接执行的模块的名字才是__main__
if __name__ == '__main__':
    x = int(input('请输入第一个正整数：'))
    y = int(input('请输入第二个正整数：'))
    print('%d和%d的公约数是%d' % (x,y,gcd(x,y)))
    print('%d和%d的公倍数是%d' % (x,y,lcm(x,y)))