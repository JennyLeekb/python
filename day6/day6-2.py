"""
实现判断一个数是不是回文数的函数。

Author:lkb
"""

def is_palindrome(num):
    temp = num 
    total = 0
    while temp > 0 :
        total = total * 10 + temp%10
        temp //= 10
    return total == num


# __name__是Python中一个隐含的变量它代表了模块的名字
# 只有被Python解释器直接执行的模块的名字才是__main__
if __name__ == '__main__':
    x = int(input('请输入一个正整数：'))
    if is_palindrome(x):
        print('%d是回文数'%x)
    else:
        print('%d不是回文数'%x)


